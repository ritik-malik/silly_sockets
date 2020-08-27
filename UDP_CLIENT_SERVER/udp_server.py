import socket
import base64
import sys

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.bind(('127.0.0.1',6969))

print('UDP server initialized...\n',s)

while True:
    
    try:
        print('\nWaiting for a connection...')
        
        data, addr = s.recvfrom(2048)
        print('Got message from ',addr,'\nMessage = ',data.decode('utf-8'))
        print('Sending reply...')
        
        s.sendto(base64.b64encode(data),addr)

    except KeyboardInterrupt:
        print('\n\nInterrupt detected, closing the server...\n')
        s.close()
        sys.exit()
