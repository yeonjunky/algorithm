#include <stdio.h>

int main(){

    char result[100];
    int O_cnt = 0;
    int test_case;
    int score = 0;

    scanf("%d", &test_case);

    for(int i=0;i<test_case;i++){

        scanf("%s", result);
        int j = 0;

        while (result[j] != '\0'){

            if(result[j] == 'O'){

                O_cnt++;
                score = score + O_cnt;
            }

            else {
                O_cnt = 0;
            }

            j++;
            
        }
        printf("%d\n", score);
        score = 0;
        O_cnt = 0;
    }
    

    return 0;
}