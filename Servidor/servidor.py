from datetime import datetime
from http import server
import socket
import sys


IP = "127.0.0.1"
PORT = 1236
HEADER_lENGTH =10
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind((IP,PORT))
print("Servidor iniciado!")
server_socket.listen(6)

socket_list = [server_socket]
clients = {}

fechaActual = datetime.now()

def Restaurar():
        print("Restaurar, llamando al servidor de replicacion")
        client_socket.close()
     

def replicar(mensaje):
    print(mensaje)
    client_socket.close()
   

while True:
    
    client_socket, direccion = server_socket.accept()
    msg = client_socket.recv(1024)
        #Recibe el mensaje del cliente 
    print(f"{fechaActual} - {direccion} - {msg.decode('utf-8')}")


    if msg.decode("utf-8") == "exit":
        server_socket.close()
        sys.exit()
    
    if msg.decode("utf-8") == "restaurar":
        print("Llamar al servidor replicacion")
        Restaurar()
    
    if msg.decode("utf-8") == "commit":
        print("replicacion")
        replicar(msg.decode("utf-8"))
    else:
        print("no se replica el objeto")
    
