#include <stdio.h>
#include <stdlib.h>

void merge(int *arr, int l, int m, int r){

    int n1 = m - l + 1;
    int n2 = r - m;
    int i, j, k;

    int arr1[n1], arr2[n2];

    for(i=0;i<n1;i++){
        arr1[i] = arr[l + i];
    }

    for(i=0;i<n2;i++){
        arr2[i] = arr[m + 1 + i];
    }

    i = 0;
    j = 0;
    k = l;

    while(i < n1 && j < n2){
        if(arr1[i] < arr2[j]){
            arr[k] = arr1[i];
            i++;
        }

        else{
            arr[k] = arr2[j];
            j++;
        }
        k++;
    }

    while(i < n1){
        arr[k] = arr1[i];
        i++;
        k++;
    }

    while(j < n2){
        arr[k] = arr2[j];
        j++;
        k++;
    }

}

int *sort(int *arr, int l, int r){
    int mid = l + (r-l) / 2;

    if(r > l){
        sort(arr, l, mid);
        sort(arr, mid+1, r);
    }

    merge(arr, l, mid, r);
    
    return arr;
}


int main(){

    int n;
    int *nums;

    scanf("%d", &n);

    nums = malloc(sizeof(int) * n);

    for(int i=0;i<n;i++){
        scanf("%d", &nums[i]);
    } 

    nums = sort(nums, 0, n - 1);

    for(int i=0;i<n;i++){
        printf("%d\n", nums[i]);
    }

    return 0;
}