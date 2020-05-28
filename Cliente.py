import xmlrpc.client
#crear un cliente del servidor
def menu(case,Cliente):
    if case==1:
        x=str(input("Ingrese nombre del archivo a crear: "))
        print(Cliente.CREATE(x))
    elif case==2:
        x=str(input("Ingrese nombre del archivo a leer: "))
        content=Cliente.READ(x)
        print(content)

    elif case==3:
        x=str(input("Ingrese nombre del archivo donde desea escribir: "))
        mode = "a"
        content = str(input("Escribe el contenido del archivo:\n"))
        overwrite=int(input("¿Sobrescribir archivo?\n1.Si\t2.No\n"))
        if overwrite==1:
            mode="w"
        resp=Cliente.WRITE(x,content,mode)
        print(resp)
    elif case == 4:
        x=str(input("Ingrese nombre ORIGINAL del archivo : "))
        y =str(input("Ingrese nombre NUEVO del archivo : "))
        resp=Cliente.RENAME(x,y)
    elif case == 5:
        x = str(input("Ingrese nombre del archivo a eliminar: "))
        resp = Cliente.REMOVE(x)
        print(resp)
    elif case == 6:
        x = str(input("Ruta del directorio (v.g. Practica5/Nombre_1/Nombre_2/.../)\n"))
        resp = Cliente.MKDIR(x)
        print(resp)
    elif case == 7:
        x = str(input("Ruta del directorio (v.g. Practica5/Nombre_1/Nombre_2/.../)\n"))
        resp = Cliente.RMDIR(x)
        print(resp)
    elif case == 8:
        #x = str(input("Ruta del directorio (v.g. Practica5/Nombre_1/Nombre_2/.../)\n"))
        lista = Cliente.READDIR()
        for files in lista:
            print("\t"+files)
    else:
        print("Opcion no valida\n")
def verMenu(Cliente):
    seguir=True
    while (seguir):
        print("Eliga una operacion:")
        print("1.Create\n2.Read\n3.Write\n4.Rename\n5.Remove\n6.Crear Directorio\n7.Crear Borrado\n8.Ver directorio")
        case=int(input("Opcion: "))
        menu(case,Cliente)
        print("Continuar?")
        cont=int(input("1.Si\t2.No\n"))
        if cont==1:
            seguir=True
        else:
            print()
            seguir= False
#The verbose option gives you debugging information useful for working out where communication errors might be happening.
with xmlrpc.client.ServerProxy('http://192.168.1.64:56432') as Cliente:
    verMenu(Cliente)