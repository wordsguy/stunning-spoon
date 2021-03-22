#include <stdio.h>

void letters (void);
int main(void)

{
    printf("Uppercasing\n");
    letters();
}



void letters (void)
{

    char s[20];
    printf(" : ");
    fgets(s, 16, stdin);
    printf(" : ");

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] >= 97 && s[i] <= 122)
        {
            printf("%c", s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
      printf("\n");
}

