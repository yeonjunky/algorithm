#include <stdio.h>

int main(){

    int a, b;
    int price;
    int sum;

    scanf("%d %d", &a, &b);
    scanf("%d", &price);

    sum = a + b;

    if(price*2 > sum){
        printf("%d", sum);
    }
    else{
        printf("%d", sum - price*2);
    }

    return 0;
}