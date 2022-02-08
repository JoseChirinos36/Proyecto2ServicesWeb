import socket

IP = "127.0.0.1"
PORT = 1234

header_server ="serveRep"
server_replicar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_replicar.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_replicar.connect((IP,PORT))
server_replicar.setblocking(False)

server_replicar.listen()


def replicar():
    print("guardar objeto")

def restaurar():
    print("enviar objeto guardado")