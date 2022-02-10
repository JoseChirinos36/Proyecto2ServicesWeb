import socket
import sys
host = '127.0.0.1'
port = 12033
BUFFERSIZE = 1024

def conexion1(msg,BUFFERSIZE):
    host1 = '192.168.1.118'
    port1 = 12034
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket1:
        socket1.connect((host1,port1))
        while True:
            socket1.send(msg.encode('utf-8'))
            print("--")
            data_1 = socket1.recv(BUFFERSIZE)
            print(data_1.decode('utf-8'))
            
            return data_1.decode('utf-8')


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket0:
    socket0.connect((host,port)) #probando conexion de forma local como un socket2
    
    while True:
        #En este input, es como decir que el commit proviene del Servidor de Aplicacion
        msg = input("ingresar palabra(commit, abort, azar) ")
        if msg == 'commit':
            socket0.send(msg.encode('utf-8'))
            #conexion1(msg,BUFFERSIZE)
        if msg == 'abort':
            socket0.send(msg.encode('utf-8'))                
        
        if msg == 'exit':
            socket0.close()
            sys.exit()
        
        data0 = socket0.recv(BUFFERSIZE)

        print(data0.decode("utf-8"))
        

