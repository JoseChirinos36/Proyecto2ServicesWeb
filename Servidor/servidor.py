from datetime import datetime
import socket
import sys

"""
Conexion como cliente
"""
IP = "127.0.0.1"
PORT = 12036
BUFFERSIZE = 1024

def conexion1():
    print("aqui va la conexion de servidor-cliente")
    
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket0:
    socket0.connect((IP,PORT))

    while True:
            msg0 = input("Ingrese palabra (commit,abort,azar, salir) ")
            
            if msg0 =='commit':
                socket0.send(msg0.encode('utf-8'))

            if msg0 =='abort':
                socket0.send(msg0.encode('utf-8'))

            if msg0 =='azar':
                socket0.send(msg0.encode('utf-8'))
            
            if msg0 =='salir':
                socket0.close()
                sys.exit()
            
            data_0 = socket0.recv(BUFFERSIZE)
            print(data_0.decode('utf-8'))
"""

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
    
"""