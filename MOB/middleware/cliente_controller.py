import sys
import xml.etree.ElementTree as ET
mytree = ET.parse('C:\\Users\\DELL PC\\Documents\\Pruebapython\\Proyecto\\bd.xml')
myroot = mytree.getroot()

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
            
            msg3 = input("Ingrese salir: ")
            myroot.append(objeto)
            mytree.write('C:\\Users\\DELL PC\\Documents\\Pruebapython\\Proyecto\\bd.xml')
            print("Se ha creado la informacion \n")
            if msg3 == "salir":
                sys.exit()

def eliminar():
    for x in myroot.findall('objeto'):
        x.remove()
        
        mytree.write('C:\\Users\\DELL PC\\Documents\\Pruebapython\\Proyecto\\bd.xml')
        print("Se ha eliminado toda la informacion")


def consultar():
       for x in myroot.findall('objeto'):
        fecha = x.find('fecha').text
        nombre =  x.find('nombre').text
        accion = x.find('accion').text
        #print(fecha,'-' ,nombre,'-', accion, '\n')
        print(f"Fecha: {fecha} - Nombre: {nombre} - Accion: {accion} ")
        
        
        
