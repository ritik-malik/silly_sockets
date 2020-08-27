import socket
import sys

var = input('Which socket TCP/UDP? (T/U) : ')

try:
    # A_INET = IPv4, SOCK_STREAM = TCP, SOCK_DGRAM = UDP
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) if var == 'T' else socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    print('Created socket successfully\n',s)

except socket.error:
    print('Failed to create socket')
    print('Error : ',socket.error)
    sys.exit()

HOST = input('Enter the IP/Website : ')
PORT = int(input('Enter the port number : '))

try:
    s.connect((HOST,PORT))
    print('Connected to',HOST,'at Port',PORT)
    
except socket.error:
    print('Failed to connect to',HOST,'at Port',PORT)
    print('Error',socket.error)
    sys.exit()
