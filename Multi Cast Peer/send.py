import socket
import struct
import sys
from form import Form

#message = 'very important data'
multicast_group = ('224.3.29.71', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(60)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

form = Form()
message = form.getSerialize()

try:

    # Send data to the multicast group
    #print ( 'sending "%s"' % message)
    sent = sock.sendto(message, multicast_group)

    # Look for responses from all recipients
    while True:
        print('esperando una respuesta')
        try:
            data, server = sock.recvfrom(160)
        except socket.timeout:
            print( 'tiempo de espera terminado, sin respuesta')
            break
        else:
            print( 'received "%s" from %s' % (data, server) )

finally:
    print('closing socket')
    sock.close()

#form = Form()
#datos = form.getSerialize()




