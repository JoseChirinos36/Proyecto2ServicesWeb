import sys
import xml.etree.ElementTree as ET
import socket

mytree = ET.parse('C:\\Users\\DELL PC\\Documents\\Proyecto2\\Proyecto2ServicesWeb\\MOB\\bd.xml')
myroot = mytree.getroot()

IP = "127.0.0.1"
PORT = 1236

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

header_msg = "cliente"

def crear():

    objetos = ET.Element("objetos")
    objeto = ET.SubElement(objetos,"objeto")
    obj_fecha = ET.SubElement(objeto,"fecha")
    obj_nombre = ET.SubElement(objeto,"nombre")
    obj_accion = ET.SubElement(objeto,"accion")
    ET.dump(objetos)
    print("fecha-nombre-accion\n")    
    while True:
            msg = input("Ingrese fecha: ")
            obj_fecha.text =str(msg) 

            msg1 = input("ingrese nombre o texto: ")
            obj_nombre.text = str(msg1)

            msg2 = input("Ingrese accion: ")
            obj_accion.text = str(msg2)
            #client_socket.send(bytes(msg.encode('utf-8')))
            msg3 = input("Ingrese salir: ")
            myroot.append(objeto)
            mytree.write('C:\\Users\\DELL PC\\Documents\\Proyecto2\\Proyecto2ServicesWeb\\MOB\\bd.xml')
            print("Se ha creado la informacion \n")
            if msg3 == "salir":
                sys.exit()

def eliminar():
    for x in myroot.findall('objeto'):
        x.remove()
        
        mytree.write('C:\\Users\\DELL PC\\Documents\\Proyecto2\\Proyecto2ServicesWeb\\MOB\\bd.xml')
        print("Se ha eliminado toda la informacion")


def consultar():
       for x in myroot.findall('objeto'):
        fecha = x.find('fecha').text
        nombre =  x.find('nombre').text
        accion = x.find('accion').text
       
        print(f"Fecha: {fecha} - Nombre: {nombre} - Accion: {accion} ")

def replicar():
    print("Mensaje enviado \n")
    message = "Replicar"
    client_socket.send(message.encode("utf-8"))
   
def restaurar():
    client_socket.send(header_msg + "Restaurar".encode("utf-8")) 
    print("prueba restaurar")

  