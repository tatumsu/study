#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <string.h>

#define FIFO_NAME "./myfifo"

int main()
{
    int res;
    int pipe_id;
    char buffer[] = "Hello world";
    if(access(FIFO_NAME,F_OK)==-1)
    {
        res = mkfifo(FIFO_NAME,O_WRONLY);
        if(res!=0)
        {
            printf("Error in creating fifo.\n");
            exit(1);
        }
    }
    pipe_id = open(FIFO_NAME,O_WRONLY);
    if(pipe_id!= -1)
    {
        if(write(pipe_id,buffer,PIPE_BUF)>0){
            close(pipe_id);
        }else{
            printf("Error in writing.\n");
            exit(1);
        }
    }
    else
    {
        printf("Error in opening.\n");
        exit(1);
    }
}
