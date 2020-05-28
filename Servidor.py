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
            with open(name+".txt","x") as file:
                return name + ".txt Creado correctamente"
                print()
        except FileExistsError:
            return "¡¡Archivo existente!!"
    Server.register_function(CREATE)

    def READ(name):
        try:
            with open(name + ".txt", "r") as file:
                return file.read()
                print()
        except FileNotFoundError:
            return "¡¡Archivo No existente!!"
    Server.register_function(READ)
    def WRITE(name,content,mode):
        try:
           with open(name + ".txt", mode) as file:
             file.write("\n"+content)
             print()
           return "Escritura completada!!"
        except FileNotFoundError:
            return "¡¡Archivo No existente!!"
    Server.register_function(WRITE)
    def RENAME(name1,name2):
        try:
            os.rename(name1+".txt",name2+".txt")
            return "Renombrado completo"
        except FileNotFoundError:
            return "¡¡Archivo No existente!!"
    Server.register_function(RENAME)

    def REMOVE(name):
        try:
            os.remove(name+".txt")
            return "Borrado completo"
        except FileNotFoundError:
            return "¡¡Archivo No existente!!"
    Server.register_function(REMOVE)

    def MKDIR(ruta):
        try:
            os.mkdir(ruta)
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


    print("Servidor iniciado")
    Server.serve_forever()

