from ast import While
import socket

IP = "127.0.0.1"
PORT = 1236

header_server ="serveRep"
server_replicar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_replicar.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_replicar.connect((IP,PORT))
server_replicar.setblocking(False)


def replicar():
    print("guardar objeto")

def restaurar():
    print("enviar objeto guardado")

while True:
#    msg = server_replicar.recv(20)
    print("Replicar")

    replicar()
    
