import socket
import sys
import base64
from _thread import start_new_thread

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

threads = 0
try:
    s.bind(('127.0.0.1',6969))
    print('Server initialized...')
except socket.error:
    print('Failed to bind...')
    print('Error : ',socket.error)
    sys.exit()

def thread_client(conn,threads):
    while True:
        data = conn.recv(2048)
        if not data:
            print('User exited...')
            threads-=1
            print('Number of threads running =',threads)
            break
        conn.sendall(base64.b64encode(data))
    conn.close()
    
s.listen(5)

while True:
    
    try:
        
        print('\nWaiting for clients to connect...')
        conn, addr = s.accept()
        print('Connected to ',addr)
        print('Starting new thread for client...')
        threads+=1
        start_new_thread(thread_client,(conn,threads,))
        print('Total threads running = ',threads)
    
    except KeyboardInterrupt:
        print('\n\nInterrupt detected, closing the server...\n')
        s.close()
        sys.exit()
