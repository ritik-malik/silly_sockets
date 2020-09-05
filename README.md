# silly_sockets
Bunch of sample codes for socket programming in python <br>

### Usage
In all the programs, client sends a str to server, which replies with the base64 encoding of the input<br>
(PS. yes, I know it can be done easily without it...)<br>


### Some basic info to fill README.md
Send the message after encoding it to `UTF-8` by using<br>
`input('Enter your message : ').encode('utf-8')`<br>
The message is received in `bytes` in both sides, `b'your message'`<br>
Decode it using,<br>
`data,addr = s.recvfrom(2048)`<br>
`data.decode('utf-8')`<br>

--------------------------------------

`s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)` <br>
`s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)`<br>
Here, `AF_INET` = IPv4<br>
`SOCK_STREAM` = TCP<br>
`SOCK_DGRAM`  = UDP<br>

--------------------------------------

`s.connect((HOST,PORT))`<br>
s.connect takes only one tuple with host (which can be URL/IP) & port <br>

##### For TCP
* `s.send()` <br>
* `s.recv(buff)` where buff is max size to receive <br>

##### For UDP
* `s.sendto()` <br>
* `s.recvfrom(buff)` <br>

##### Something new for me
[Sending an empty msg in a socket](https://stackoverflow.com/questions/3363395/how-to-receive-a-socket-message-with-an-empty-data)

##### And as always, a tree
┌─[michael@VSauce]─[~/Desktop/silly_sockets] <br>
└──╼ $tree <br>
. <br>
├── MULTI_THREADED <br>
│   ├── client.py <br>
│   └── multithread_server.py <br>
├── README.md <br>
├── TCP_CLIENT_SERVER <br>
│   ├── tcp_client.py <br>
│   └── tcp_server.py <br>
├── TCP_UDP_SOCK <br>
│   └── tcp_udp_sock.py <br>
└── UDP_CLIENT_SERVER <br>
    ├── udp_client.py <br>
    └── udp_server.py <br>
<br>
4 directories, 8 files <br>


