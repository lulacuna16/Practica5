from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import shutil


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('192.168.1.64', 56432),requestHandler=RequestHandler) as Server:
    Server.register_introspection_functions()

    def CREATE(name):
        try:
            with open(name,"x") as file:
                return name + " Creado correctamente"
                print()
        except FileExistsError:
            return "¡¡Archivo existente!!"
        except FileNotFoundError:
            return "¡¡Ruta no existente!!"
    Server.register_function(CREATE)

    def READ(name):
        try:
            with open(name, "r") as file:
                return file.read()
                print()
        except FileNotFoundError:
            return "¡¡Archivo/Ruta No existente!!"
    Server.register_function(READ)
    def WRITE(name,content,mode):
        try:
           with open(name, mode) as file:
             file.write("\n"+content)
             print()
           return "Escritura completada!!"
        except FileNotFoundError:
            return "¡¡Archivo/Ruta No existente!!"
    Server.register_function(WRITE)
    def RENAME(name1,name2):
        try:
            os.rename(name1,name2)
            return "Renombrado completo"
        except FileNotFoundError:
            return "¡¡Archivo/Ruta No existente!!"
    Server.register_function(RENAME)

    def REMOVE(name):
        try:
            os.remove(name)
            return "Borrado completo"
        except FileNotFoundError:
            return "¡¡Archivo/Ruta No existente!!"
    Server.register_function(REMOVE)

    def MKDIR(ruta):
        try:
            os.makedirs(ruta)
            return "Directorio creado"
        except FileNotFoundError:
            return "¡¡Ruta Invalida!!"
        except FileExistsError:
            return "¡¡Ruta existente!!"
    Server.register_function(MKDIR)

    def RMDIR(ruta):
        try:
            shutil.rmtree(ruta)
            return "Directorio borrado"
        except FileNotFoundError:
            return "¡¡Ruta Invalida!!"
        except FileExistsError:
            return "¡¡Ruta existente!!"
    Server.register_function(RMDIR)
    def READDIR():
        try:
            lista=os.listdir()
            return lista
        except FileNotFoundError:
            return "¡¡Ruta Invalida!!"
    Server.register_function(READDIR)
    def READDIR2(ruta):
        try:
            lista=os.listdir(ruta)
            return lista
        except FileNotFoundError:
            return "¡¡Ruta Invalida!!"
    Server.register_function(READDIR2)



    print("Servidor iniciado")
    Server.serve_forever()

