#include <stdio.h>
#include <stdlib.h>
char* magic="0123456789abcdefg";
char* format="acnt{}";
char key[0x10];
char account[0x10];
int check(char* account,char* key)
{
    int i=0;
    for(i=0;i<0x5;i++)
    {
        if(account[i]!=format[i])
        {
            return 0;
        }
    }
    if(account[0x0f]!='}')
    {
        return 0;
    }
    for(i=0;i<0x10;i++)
    {
        if(account[i]+key[i]!=magic[i])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{

    scanf("%s",account);
    scanf("%s",key);
    if(check(account,key)==1)
    {
        printf("You Win\n");
    }
    else {
        printf("You suck\n");
    }
}