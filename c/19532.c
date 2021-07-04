#include <stdio.h>

int main(){

    int a, b, c, d, e, f;
    int x, y;

    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);

    if((b * e) * (b * e) > 0){
        // printf("%d / %d\n",(e * c - b * f),(a * e - d * b));
        x = (e * c - b * f) / (a * e - d * b);
    }
    else{
        // printf("%d / %d\n",(e * c + b * f),(a * e + d * b));
        x = (e * c + b * f) / (a * e + d * b);
    }

    if((a * d)*(a * d) > 0){
        // printf("%d / %d\n",(d * c - a * f),(d * b - a * e));
        y = (d * c - a * f) / (d * b - a * e);
    }
    else{
        // printf("%d / %d\n",(d * c + a * f),(d * b + a * e));
        y = (d * c + a * f) / (d * b + a * e);
    }

    printf("%d %d\n", x, y);

    return 0;
}