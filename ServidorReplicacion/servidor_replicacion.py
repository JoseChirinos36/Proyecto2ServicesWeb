import socket
import sys
from xmlrpc.client import ResponseError

replicaSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print("Esperando conexion")
try:
    replicaSocket.connect((host,port))
except socket.error as e:
    print(str(e))

Response = replicaSocket.recv(1024)
while True:
    msg = input('Say something: ')
    replicaSocket.send(msg.encode('utf-8'))
    Response = replicaSocket.recv(1024)
    print(Response.decode('utf-8'))

    if msg == 'exit':
        replicaSocket.close()
        sys.exit()

    replicaSocket.close()