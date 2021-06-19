#include <stdio.h>

int main(){

    int t;
    int a, b;
    int num;

    scanf("%d", &t);

    for(int i=0;i<t;i++){
        num = 1;

        scanf("%d %d", &a, &b);

        for(int j=0;j<b;j++) num = (num * a) % 10;

        if (num == 0) printf("10\n");
        else printf("%d\n", num);
    }

    return 0;
}