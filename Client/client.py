'''
    UDP socket client
    
'''
import socket   #para usar sockets
import sys      #para entrada de datos
from form import Form #Formulario 

 
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
b=True
while(b) :
    msg = 'nombre: '+nombre+' apellido: '+apellido+' ci: '+ci+' fecha de Nacimiento: '+f_n+' lugar de nacimiento: '+lugar_n
     
    try :
        #Set the whole string
        s.sendto(msg.encode(), (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print ('Server reply : ' + reply.decode())
        b=False
    except socket.error as msg:
        print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()