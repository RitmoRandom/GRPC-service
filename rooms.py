from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
import sqlite3
import os
import requests

db_path = 'rooms.db'

# Implementación del servicio gRPC
class MyService(service_pb2_grpc.MyServiceServicer):
    
    # Registrar una nueva habitación
    def RegisterRoom(self, request, context):
        if request.room_number == 0:
            context.set_details("room_number cannot be 0")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return service_pb2.RegisterRoomResponse()
        
        try:
            if not os.path.exists(db_path):
                context.set_details("base de datos no encontrada")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return service_pb2.RegisterRoomResponse()
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO rooms (room_number, room_type, status) 
                    VALUES (?, ?, ?)
                ''', (request.room_number, request.room_type, request.status))
                conn.commit()
            room_id = cursor.lastrowid
            url = 'http://localhost:5000/?wsdl'
            # Encabezados de la solicitud (si es necesario)
            headers = {
                'Content-Type': 'text/xml',
            }

            # Cuerpo de la solicitud SOAP en formato XML
            soap_request_template = '''<?xml version='1.0' encoding='UTF-8'?>
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spyne="spyne.examples.availability">
                <soapenv:Body>
                    <spyne:add_availability>
                        <spyne:room_id>{param1}</spyne:room_id>
                        <spyne:room_type>{param2}</spyne:room_type>
                    </spyne:add_availability>
                </soapenv:Body>
            </soapenv:Envelope>'''
            soap_request = soap_request_template.format(param1=room_id, param2=request.room_type)
            response = requests.post(url, data=soap_request, headers=headers)
            print(response.text)
            return service_pb2.RegisterRoomResponse(message=f"Room registered successfully with ID: {room_id}", room_id=room_id)
        except Exception as e:
            context.set_details(f"Error: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return service_pb2.RegisterRoomResponse()
        
        

    # Actualizar el estado de la habitación
    def UpdateRoomStatus(self, request, context):
        if request.room_id == 0:
            context.set_details("room_id cannot be 0")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return service_pb2.UpdateRoomStatusResponse()
        try:
            if not os.path.exists(db_path):
                context.set_details("base de datos no encontrada")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return service_pb2.UpdateRoomStatusResponse()
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE rooms SET status = ? WHERE room_id = ?
                ''', (request.status, request.room_id))
                conn.commit()
            return service_pb2.UpdateRoomStatusResponse(message="Room status updated successfully")
        except Exception as e:
            context.set_details(f"Error: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return service_pb2.UpdateRoomStatusResponse()
        

    # Obtener una habitación por su ID
    def GetRoomById(self, request, context):
        try:
            if not os.path.exists(db_path):
                context.set_details("base de datos no encontrada")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return service_pb2.GetRoomByIdResponse()
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM rooms WHERE room_id = ?', (request.room_id,))
                row = cursor.fetchone()
            if row:
                return service_pb2.GetRoomByIdResponse(
                    room_id=row[0],       # room_id es el primer campo en la tupla
                    room_number=row[1],   # room_number es el segundo campo
                    room_type=row[2],     # room_type es el tercer campo
                    status=row[3]         # status es el cuarto campo
                )
            else:
                context.set_details(f"Room with ID {request.room_id} not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return service_pb2.GetRoomByIdResponse()  # Retorna una respuesta vacía
        except Exception as e:
            context.set_details(f"Error: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return service_pb2.GetRoomByIdResponse()
    
    # Obtener una habitación por su ID
    def GetRoomByNum(self, request, context):
        try:
            if not os.path.exists(db_path):
                context.set_details("base de datos no encontrada")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return service_pb2.GetRoomByNumResponse()
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM rooms WHERE room_number = ?', (request.room_number,))
                row = cursor.fetchone()
            if row:
                return service_pb2.GetRoomByNumResponse(
                    room_id=row[0],       # room_id es el primer campo en la tupla
                    room_number=row[1],   # room_number es el segundo campo
                    room_type=row[2],     # room_type es el tercer campo
                    status=row[3]         # status es el cuarto campo
                )
            else:
                context.set_details(f"Room with number {request.room_number} not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return service_pb2.GetRoomByNumResponse()  # Retorna una respuesta vacía
        except Exception as e:
            context.set_details(f"Error: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return service_pb2.GetRoomByNumResponse()
        

def init_db():
    """Inicializa la base de datos SQLite y crea la tabla si no existe."""
    if not os.path.exists(db_path):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rooms (
                    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_number INTEGER NOT NULL,
                    room_type TEXT NOT NULL,
                    status TEXT NOT NULL
                );
            ''')
            # Insertar datos de ejemplo
            cursor.executemany('''
                INSERT INTO rooms (room_number, room_type, status) VALUES (?)
            ''', [(101,"Single","available"), (105,"Doble","available"), (108,"Single","available")])
            conn.commit()
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server running on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    init_db()
    serve()