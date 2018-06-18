'''
    UDP socket Server
'''
import time
import socket
import sys
import pickle # decodificar objeto loads()
from datetime import datetime, date


formato_fecha = "%d-%m-%Y"
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)



while True:
    # Wait for a connection
    print  ('Esperando por una Conexion')
    connection, client_address = sock.accept()
    try:
        print ('conectado con', client_address)

            # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(420)
            print  ('recibido ',len(data))

            if data:
                obj = pickle.loads(data)
                fecha = obj['fecha_n']
                fecha_inicial = datetime.strptime(fecha, formato_fecha)
                hoy = datetime.now()
                edad = (hoy - fecha_inicial ).days /365
                edad = int(edad)
                nombre = obj['nombre']
                print('Nombre: ',nombre)
                print('edad',edad)
                print('recibiendo archivo..')
                foto_archivo = open('foto_name.png','wb')
                close = True
                tam = 0
                while close:
                    rec = connection.recv(420)
                    tam += len(rec)
                    if rec == b'fin':
                        close =False
                    foto_archivo.write(rec)
                

                foto_archivo.close()
                time.sleep(5)
                print('archivo recibido: ',str(tam),'bytes')
                print  (' enviando datos al cliente')
                response = 'Hola '+nombre+ ' de ' + str(edad)+' a#os.'
                connection.sendall(response.encode())
            else:
                print  ('no hay datos del cliente', client_address)
                break
                
    finally:
            # Clean up the connection
        connection.close()
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

'''
