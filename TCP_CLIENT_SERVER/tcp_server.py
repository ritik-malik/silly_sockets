import socket
import base64
import sys

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('127.0.0.1',6969))
s.listen(5)

print('TCP server initialized...\n',s)
i=0

while True:
    
    try:
        print('\nWaiting for clients to connect...')
        conn, addr = s.accept()
        print('Client number',i,'conencted...')
        i+=1
        
        while True:
            try:
                data = conn.recv(1024)  #.decode('utf-8')
                if not data:
                    print('User exited...')
                    break
                print('Got message from',addr,'\nMessage = ',data.decode('utf-8'),'\nSending reply...\n')
                conn.send(base64.b64encode(data))
            except:
                print('User exited...')
                conn.close()
                break
            
    except KeyboardInterrupt:
        print('\n\nInterrupt detected, closing the server...\n')
        s.close()
        sys.exit()
