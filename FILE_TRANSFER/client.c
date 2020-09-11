#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libgen.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <errno.h>

int main(){

    int sockfd = 0;
    int bytesReceived = 0;
    char revcBuff[256];
    char f_name[20];

    memset(revcBuff, '0', sizeof(revcBuff));
    struct sockaddr_in serv_addr;

    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        printf("Error creating socket");
        return 1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(20000);
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if(connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0){
        printf("Failed to connect\n");
        return 1;
    }

    printf("\nConnected to server successfully!\nEnter the filef_name: ");
    scanf("%[^\n]%*c",f_name);
    printf("\n");

    write(sockfd, f_name, sizeof(f_name));

    bytesReceived = read(sockfd, revcBuff, sizeof(revcBuff));
    
    // printf("Recv buffer is %s\n",revcBuff);

    if(strcmp("NF",revcBuff) == 0){
            printf("Error: File not found...\n");
            close(sockfd);
            return 0;
        }

    else{
        
        FILE *fp = fopen(f_name, "ab");

        while(1){

        if(strcmp("END",revcBuff) == 0){

        printf("END signal received, closing the connection...\n");
        close(sockfd);
        return 0;
        }

        // printf("Bytes received %d\n", bytesReceived);

        fwrite(revcBuff, 1, bytesReceived, fp);

        bzero(revcBuff, sizeof(revcBuff));
        bytesReceived = read(sockfd, revcBuff, sizeof(revcBuff));
         
        // printf("new recvBuff is = %s\n",revcBuff);

        }
    }
    
    return 0;

}











































