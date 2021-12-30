#include <stdio.h>

int factorial(int n){
    if(n == 0){
        return 0;
    }

    else if(n == 1){
        return 1;
    }

    return factorial(n-1) + factorial(n-2);
}

int main(){

    int n;

    scanf("%d", &n);
    printf("%d\n", factorial(n));

    return 0;
}