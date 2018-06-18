from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime, date # control para las fechas
import xmlrpc.client
import random


list_avatar = ['chica128','chico64','estudiante128','hombre128','hombre-negocios64','hombre-negocios128' ]

formato_fecha = "%d-%m-%Y"

def serverForm(nombre,apellido,ci,f_n,lugar,foto):
    
    fecha = f_n
    fecha_inicial = datetime.strptime(fecha, formato_fecha)
    hoy = datetime.now()
    edad = (hoy - fecha_inicial ).days /365
    edad = int(edad)
    nombre = nombre
    print('formulario recibido: ', nombre, apellido, ci,f_n, lugar)

    with open("fetched_foto.png", "wb") as handle:
    	handle.write(foto.data)
    	tam = len(foto.data)
    
    respuesta = 'hola %s, edad: %s a#os' % (nombre,edad)
    print ('foto revibida: ',tam,'bytes')
    return respuesta

def python_logo():
	aleatorio = random.randint(0,5)
	avatar  = 'media/' + list_avatar[aleatorio] + '.png'
	print('enviando avatar...')
	with open(avatar, "rb") as handle:
		return xmlrpc.client.Binary(handle.read())

# A simple server with simple arithmetic functions
server = SimpleXMLRPCServer(("localhost", 8000))
print("escuchando port 8000...")

server.register_function(serverForm,'formulario')
server.register_function(python_logo,'foto')
server.serve_forever()