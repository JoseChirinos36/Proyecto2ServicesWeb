import socket
import sys

host = '127.0.0.1' #192.168.1.118 (si se conecta con el server en una maquina virtual)
port = 12033
BUFFERSIZE = 1024

print("prueba del servidor")
socket0 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket0.bind((host,port))
socket0.listen(6)

coor, adr = socket0.accept()

def replicarObjeto():
    print("replicar")

while True:
    print(f"Conexion establecida por: {adr}")
    data0 = coor.recv(BUFFERSIZE)
    print(data0.decode('utf-8'))

    if data0.decode('utf-8') == 'commit':
        print("Preparandose para replicar") #Deberia llamar a un metodo para hacer el proceso
        msg = "VOTE_COMMIT"
        coor.send(msg.encode('utf-8'))

    if data0.decode('utf-8') == 'abort':
        print("Enviar mensaje de rechazar objeto") #envia el abort 
        msg = "VOTE_ABORT"
        coor.send(msg.encode('utf-8'))

    #Como dice aqui es para salir del server
    if data0.decode('utf-8')== 'salir':
        coor.close()
        sys.exit()

    msg = "hola desde win10, fisica, server"
    coor.send(msg.encode('utf-8'))

    
  

    

"""
def replicarObjeto():
        print("replicando objeto")

"""