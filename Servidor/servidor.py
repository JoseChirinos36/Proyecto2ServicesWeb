from datetime import datetime
import socket
import sys
import time


IP = "127.0.0.1"
PORT = 1236

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind((IP,PORT))
print("Servidor iniciado!")
server_socket.listen()

fechaActual = datetime.now()

def Restaurar():
        print("Restaurar, llamando al servidor de replicacion")
        sys.exit()


while True:
    #Acepta la conexion del cliente
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

    



