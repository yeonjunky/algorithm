#include <stdio.h>

int main(){

    int C;
    float N;
    int score[1000];
    int sum = 0;
    float cnt = 0;
    float avr = 0;
    float percent = 0;

    scanf("%d", &C);

    for(int i=0;i<C;i++){

        scanf("%f", &N);

        for(int j=0;j<N;j++){

            scanf("%d", &score[j]);
            sum = sum + score[j];

        }

        avr = sum / N;

        for(int j=0;j<N;j++){

            if(score[j] > avr){
                cnt++;
            }

        }

        percent = cnt / N * 100;
        printf("%.3f%%\n", percent);

        cnt = 0;
        sum = 0;

    }



    return 0;
}