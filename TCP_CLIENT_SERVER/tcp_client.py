import socket
import sys

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.connect(('127.0.0.1',6969))
print('Connected to server...')

while True:
    
    try:
        data = input('Enter the text to be encoded : ').encode('utf-8')
        s.send(data)
        out = s.recv(1024).decode('utf-8')
        print('Text in base64 is : ',out,'\n')
    except KeyboardInterrupt:
        print('\n\nInterrupt detected, closing the connection...\n')
        s.close()
        sys.exit()
