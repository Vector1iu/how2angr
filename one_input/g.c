#include <stdio.h>
#include <stdlib.h>

char *format="flag{";
char *magic="WBRDEFGHIJ";
char key[0x10];

int ischeck(char* key)
{
    if(strncmp(key,format,strlen(format)))
    {
        return 0;
    }
    if(key[strlen(key)-1]!='}')
    {
        return 0;
    }
    int i=0;
    //printf("-------");
    for(i=0;i<10;i++)
    {
        if(key[i+5]+1!=magic[i])
        {
            printf("%d",i);
            return 0;
        }
    }
    return 1;
}

int main()
{
    scanf("%16s",key);
    if(ischeck(key) == 1)
    {
        printf("You win\n");
    }
    else
    {
        printf("You suck\n");
    }
    return 0;
}