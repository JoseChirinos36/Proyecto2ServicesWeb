from datetime import datetime
import socket
import sys
import time
import select


IP = "127.0.0.1"
PORT = 1236
HEADER_lENGTH =10
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind((IP,PORT))
print("Servidor iniciado!")
server_socket.listen()

socket_list = [server_socket]
clients = {}

fechaActual = datetime.now()

def Restaurar():
        print("Restaurar, llamando al servidor de replicacion")
        sys.exit()

def replicar(mensaje):
    print("replicar")


def recieve_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_lENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

    for notified_socket in read_sockets:
        #Acepta la conexion del cliente
        if notified_socket == server_socket:
            client_socket, direccion = server_socket.accept()
        


    #Recibe el mensaje del cliente 
    mensaje = client_socket.recv(1024)
    print(f"{fechaActual} - {direccion[0]}")


    if mensaje.decode("utf-8") == "exit":
        server_socket.close()
        sys.exit()
    
    if mensaje.decode("utf-8") == "restaurar":
        print("Llamar al servidor replicacion")
        Restaurar()
    
    if mensaje.decode("utf-8") == "replicar":
        print("replicacion")
        replicar(mensaje.decode("utf-8"))

    



