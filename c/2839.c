#include <stdio.h>

int main(){

    int n, cnt = 0, result=0;

    scanf("%d", &n);

    while(n > 0){
        if(n % 5 == 0){
            n -= 5;
            cnt++;
        }
        else if(n % 3 == 0){
            n -= 3;
            cnt++;
        }
        else if(n > 5){
            n -= 5;
            cnt++;
        }
        else if(n % 3 != 0 && n < 5){
            result = 1;
            break;
        }
    }

    if(result){
        printf("-1\n");
    }
    else{
        printf("%d\n", cnt);
    }

    return 0;
}