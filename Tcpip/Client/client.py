'''
    TCP socket client
    
'''
import time
import socket
import sys
from form import Form #Formulario

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.101', 10000)
print  ('conectando a %s puerto %s' % server_address)
sock.connect(server_address)

formulario = Form()
obj = formulario.getSerialize()
foto = formulario.getFotoArray()
try:
    
    # Send data
    print ('enviando.. datos y foto'  )
    sock.sendall(obj)

    for f in foto:
        
        sock.sendall(f)
        time.sleep(3)
    # Look for the response
    amount_received = 0
    amount_expected = len(obj)
    
    while amount_received < amount_expected:
        data = sock.recv(400)
        amount_received += len(data)
        print ('received "%s"' % data.decode())
        break

finally:
    print ('cerrando socket')
    sock.close()

''' 
import socket   #para usar sockets
import sys      #para entrada de datos
from form import Form #Formulario 
import pickle #serializacion y codificacion function dumbs() and loads()
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Falla al Crear Socket')
    sys.exit()
 
host = 'localhost';
port = 7890;

formulario = Form()
nombre = formulario.getName()
apellido = formulario.getLastName()
ci = formulario.getCI()
f_n = formulario.getDate()
lugar_n = formulario.getPlace()
f_array = formulario.getFotoArray() #bytes de la foto 
#array de bytes de la foto
obj = formulario.getSerialize()
b=True
while(b) :
    
    try :
        #Set the whole string
        s.sendto(obj, (host, port)) #msg.encode()
        # for x in f_array:
        #     s.sendto(x, (host, port))
        #s.sendto('fin'.encode(), (host, port))
        #s.sendto(foto, (host, port))
         
        #receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print ('Server reply : ' + reply.decode())
        b=False
    except socket.error as msg:
        print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
'''