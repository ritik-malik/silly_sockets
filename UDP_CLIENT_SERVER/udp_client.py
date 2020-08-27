import socket
import sys

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

while True:
    try:
        msg = input('Enter your message : ').encode('utf-8')
        s.sendto(msg,('127.0.0.1',6969))
        data,addr = s.recvfrom(2048)
        print(data.decode('utf-8'))
    
    except KeyboardInterrupt:
        print('\n\nInterrupt detected, closing the connection...\n')
        s.close()
        sys.exit()
