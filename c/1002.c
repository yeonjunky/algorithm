#include <stdio.h>
#include <math.h>

int main(){

    int x1, y1, r1, x2, y2, r2;
    double d;
    int test_case;

    scanf("%d", &test_case);

    for(int i=0;i<test_case;i++){
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

        d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

        if (d == 0 && r1 == r2){
            printf("-1\n");
        }

        else if (d > r1 + r2 || (d == 0 && r1 != r2) || r1 > d + r2 || r2 > d + r1){
            printf("0\n");
        }

        else if (d == r1 + r2 || r1 == d + r2 || r2 == d + r1){
            printf("1\n");
        }

        else if(d < r1 + r2){
            printf("2\n");
        }
    }
    return 0;
}