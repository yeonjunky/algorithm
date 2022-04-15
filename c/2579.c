#include <stdio.h>

#define SIZE 300
#define max(a, b) (((a) > (b)) ? (a) : (b))

int main(){

    int n;
    int score;
    int scores[SIZE];
    int dp[SIZE];

    scanf("%d", &n);

    for(int i=0;i<n;i++){
        scanf("%d", &score);
        scores[i] = score;
    }

    dp[0] = scores[0];
    dp[1] = max(scores[1] + scores[0], scores[0]);
    dp[2] = max(scores[2] + scores[0], scores[2] + scores[1]);

    for(int i=3;i<n;i++){
        dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i] + scores[i - 1]);
    }

    printf("%d\n", dp[n - 1]);

    return 0;
}