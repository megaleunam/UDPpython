'''
    UDP socket Server
'''
 
import socket
import sys
import pickle # decodificar objeto loads()
from datetime import datetime, date

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 7890 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
except socket.error as msg:
    print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
formato_fecha = "%d-%m-%Y"
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(224)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break

    try:
        print(len(data))
        obj = pickle.loads(data)
        fecha = obj['fecha_n']
        fecha_inicial = datetime.strptime(fecha, formato_fecha)
        hoy = datetime.now()
        edad = (hoy - fecha_inicial ).days /365
        edad = int(edad)
        nombre = obj['nombre']
        print('edad',edad)
        print ('Message[' + addr[0] + ':' + str(addr[1]) + '] - ', obj, ' tam: ')
    except UnicodeDecodeError as e:
        print ('Message[' + addr[0] + ':' + str(addr[1]) + '] - ', data)

    ciclo = True
    foto_archivo = open('foto_name.png','wb')
    while ciclo:

        if data != b'fin':
            d = s.recvfrom(1024)
            data = d[0]
            addr = d[1]
            foto_archivo.write(data)
        else:
            foto_archivo.close()
            break
                

    #reply = 'OK...' + data.decode()
     
    #s.sendto(reply.encode() , addr)
    
    try:
        print ('Message[' + addr[0] + ':' + str(addr[1]) + '] - ', data)
    except UnicodeDecodeError as e:
        print ('Message[' + addr[0] + ':' + str(addr[1]) + '] - ', data)
    response = 'Hola '+nombre+ ' de ' + str(edad)+' años.'  
    s.sendto(response.encode() , addr)
    break

s.close()
