#include <stdio.h>

int main(){

    int n;
    int num_student, num_apple;
    int sum = 0;

    scanf("%d", &n);

    for(int i=0;i<n;i++){
        scanf("%d %d", &num_student, &num_apple);
        if(num_apple >= num_student){
            sum = sum + num_apple % num_student;
        }

        else{
            sum = sum + num_apple;
        }
    }
    printf("%d", sum);
    return 0;
}