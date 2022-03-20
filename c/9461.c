#include <stdio.h>

#define SIZE 101

int main() {

    int t, n;
    

    scanf("%d", &t);


    for(int i=0;i<t;i++){
        unsigned long dp[SIZE];
        dp[0] = dp[1] = dp[2] = 1;

        scanf("%d", &n);

        for(int j=3;j<n;j++){
            dp[j] = dp[j - 2] + dp[j - 3];
        }
        printf("%ld\n", dp[n - 1]);
    }

    return 0;
}