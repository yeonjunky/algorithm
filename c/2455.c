#include <stdio.h>

int main(){
    int in, out;
    int num = 0;
    int max = 0;

    for(int i=0;i<4;i++){
        scanf("%d %d", &out, &in);
        num = num + in - out;
        if(max < num){
            max = num;
        }
    }
    printf("%d", max);

    return 0;
}