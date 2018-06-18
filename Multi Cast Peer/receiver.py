import socket
import struct
import sys
import pickle
from datetime import date, datetime

multicast_group = '224.3.29.71'
server_address = ('', 10000)
formato_fecha = "%d-%m-%Y"
# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
lista_user = []
while True:
    print( '\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    
    print('received %s bytes from %s' % (len(data), address) )
    
    obj = pickle.loads(data)
    fecha = obj['fecha_n']
    fecha_inicial = datetime.strptime(fecha, formato_fecha)
    hoy = datetime.now()
    edad = (hoy - fecha_inicial ).days /365
    edad = int(edad)
    datos = 'usuario: '+str(address[0])+', edad:'+str(edad)
    print('enviando datos: ',datos)
    print( 'nuevo miembro conectado', address)
    msj ='Usted de edad: '+str(edad)+'a#os, se ha conectado al grupo'
    sock.sendto(msj.encode(), address)
    for u in lista_user:
     	sock.sendto(datos.encode(), u)
    lista_user.append(address)

# while True:
#     data, address = sock.recvfrom(255)
#     print (address)
#     obj = pickle.loads(data)
#     fecha = obj['fecha_n']
#     fecha_inicial = datetime.strptime(fecha, formato_fecha)
#     hoy = datetime.now()
#     edad = (hoy - fecha_inicial ).days /365
#     edad = int(edad)
#     datos = 'usuario: '+str(address[0])+', edad:'+str(edad)
#     sock.sendto(datos.encode(), (multicast_addr, port))