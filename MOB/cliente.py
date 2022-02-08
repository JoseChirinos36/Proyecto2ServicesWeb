import sys
from middleware.cliente_controller import * 
import socket

IP = "127.0.0.1"
PORT = 1236
option = ''
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

def replicar():
    print("POR HACER")

while(option !='6'):
    print("Inicio\n ")
    print("[1] Crear informacion\n") 
    print("[2] Consultar informacion\n")
    print("[3] Eliminar informacion\n")
    print("[4] Replicar informacion\n")
    print("[5] Restaurar informacion\n")
    print("[6] Salir\n")

    option = input('Ingrese su opcion:  ')
    print("\n")
    if(option == '1'):
        crear()
    elif(option == '2'):
        consultar()
    elif(option == '3'):
        eliminar()
    elif(option== '4'):
        replicar()
    elif(option== '5'):
        client_socket.send("Restaurar".encode("utf-8"))   
    elif(option== '6'):
        client_socket.send("exit".encode("utf-8"))
        sys.exit()

