import socket
import sys
host0 = '127.0.0.1'
port0 = 12036
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

def conexion2(msg):
    host2 = '127.0.0.1'
    port2 = 12033
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket2:
        socket2.connect((host2,port2)) #probando conexion de forma local como un socket2
        
        while True:
            #msg recibe la informacion del server
           
            if msg == 'commit':
                socket2.send(msg.encode('utf-8'))
                
            if msg == 'abort':
                socket2.send(msg.encode('utf-8'))                
            
            if msg == 'exit':
                socket2.close()
                sys.exit()
            
            data2 = socket2.recv(BUFFERSIZE)

            print(data2.decode("utf-8"))


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket0:
    socket0.bind((host0,port0))
    socket0.listen(6)

    client, adr = socket0.accept()

    print("Inicio Servidor..") 
    while True:
        print(f"Conexion establecida - {adr}")

        data_0 = client.recv(BUFFERSIZE)
        print(data_0.decode("utf-8"))
        if data_0.decode("utf-8")=='commit':
            conexion2(data_0) #llamando al Servidor_Replicacion
        msg0 = "Soy el coordinador"

        client.send(msg0.encode('utf-8'))
