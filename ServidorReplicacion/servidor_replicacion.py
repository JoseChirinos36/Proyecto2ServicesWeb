from ast import While
import socket

IP = "127.0.0.1"
PORT = 1236

header_server ="serveRep"
server_replicar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_replicar.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_replicar.connect((IP,PORT))
server_replicar.setblocking(False)

server_replicar.listen()

server_replicar.send(header_server.encode('utf-8'))


msg =  server_replicar.recv(1024)
def replicar():
    print("guardar objeto")

def restaurar():
    print("enviar objeto guardado")

while True:
    if msg.decode("utf-8") == "Replicar":
        print("Replicar")
        archivo = server_replicar.recv(1024)
    
