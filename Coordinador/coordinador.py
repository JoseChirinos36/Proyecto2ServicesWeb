import socket
import os
from _thread import *

serverSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    serverSocket.bind((host,port))
except socket.error as e:
    print(str(e))

print("Esperando por conexion..")
serverSocket.listen(5)

def thread_client(connection):
    connection.send(str.encode('Bienvenido al servidor'))
    while True:
        data = connection.recv(2048)
        reply = 'Server says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    client, address = serverSocket.accept()
    print("Connected to: "+ address[0] + ":" + str(address[1]))
    start_new_thread(thread_client,(client, ))
    ThreadCount += 1
    print("Thread Number: " + str(ThreadCount))

serverSocket.close()

