import sys
from modules.cliente_controller import * 
option = ''


while(option !='6'):
    print("Inicio\n ")
    print("[1] Crear informacion\n") 
    print("[2] Consultar informacion\n")
    print("[3] Eliminar informacion\n")
    print("[4] Replicar informacion\n")
    print("[5] Restaurar informacion\n")
    print("[6] Salir\n")

    option = input('Ingrese su opcion:  ')
    print("\n")
    if(option == '1'):
        crear()
    elif(option == '2'):
        consultar()
    elif(option == '3'):
        eliminar()
    elif(option== '4'):
        replicar()
    elif(option== '5'):
       print("Restaurar, por hacer")
    elif(option== '6'):
        print("Saliendo del programa")
        sys.exit()

