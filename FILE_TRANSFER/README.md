## File transfer
Transfer file from remote server to client, using TCP sockets in C

### Assumptions : 
1. The folder in which server looks for files is the same folder where server.c is located
2. Once the file is transferred, client disconnects while server wait for anotherconnection
3. The max packet size for transferring file is chosen 256 bytes

### Example : 
Requested the server.c file as itself from the sever <br>
The wireshark screenshot confirms the data of server.c (the header files) being transferred
