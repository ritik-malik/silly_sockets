#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(){

    int size = 0;
    int listenfd = 0;
    int connfd = 0;
    char msg_buff[80];
    char FLAG[] = "NF";
    char END[] = "END";

    struct sockaddr_in server_addr, client_addr;
    char sendBuff[1025];
    size = sizeof(client_addr);

    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    printf("Server initiated successfully...\n");

    memset(&server_addr, '0', sizeof(server_addr));
    memset(sendBuff, '0', sizeof(sendBuff));

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(20000);

    bind(listenfd, (struct sockaddr*)&server_addr, sizeof(server_addr));

    if(listen(listenfd,10) == -1){
        printf("Failed to listen\n");
        return -1;
    }

    while (1)
    {
        printf("\nListening for connections...\n");
        connfd = accept(listenfd, (struct sockaddr*)&client_addr, &size);
        printf("Connected to client!\n");

        // read msg from client

        read(connfd, msg_buff, sizeof(msg_buff));
        printf("Filename requested by client = %s\n",msg_buff);

        if( access( msg_buff, F_OK ) != -1 ) {
            
            // file exists
            printf("File exist!\nReading file...\n");
            FILE *fp = fopen(msg_buff,"rb");
            
            while (1)
            {
                 // read file
                unsigned char buff[256] = {0};
                int fdata = fread(buff, 1, 256, fp);

                printf("Sending data in chunks...\n");

                write(connfd, buff, fdata);

                if(fdata == 0){
                    printf("Reached EOF, sending END signal\nFile transferred successfully!\n");
                    write(connfd, END, sizeof(END));
                    break;
                }

            }
            
        } 
        
        else {
            // file doesn't exist
            printf("File doesn't exist!\n");
            write(connfd, FLAG, sizeof(FLAG));
        }


    }
    
    return 0;

}

















































