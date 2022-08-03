#include <stdio.h>

int main(){
    int n;
    int nums[10001] = {0};

    scanf("%d", &n);

    for(int i=0;i<n;i++){
        short idx;
        scanf("%hd", &idx);
        nums[idx] = nums[idx] + 1;
    }

    for(int i=0;i<10001;i++){
        for(int j=0;j<nums[i];j++){
            printf("%d\n", i);
        }
    }

    return 0;
}