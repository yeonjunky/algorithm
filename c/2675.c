#include <stdio.h>
#include <stdlib.h>

int len(char *str);

int main(){

    int t, r;
    char s[20];
    char *result;
    size_t size;

    scanf("%d", &t);

    for(int i=0;i<t;i++){
        scanf("%d %s", &r, s);

        size = len(s) * r + 1;

        result = malloc(size);

        for(int j=0;j<len(s);j++){
            for(int k=0;k<r;k++){
                result[j * r + k] = s[j];
            }
        }
        result[size] = '\0';
        printf("%s\n", result);
    }
    return 0;
}

int len(char *str){
    int i = 0;
    while(str[i] != '\0'){
        i++;
    }
    return i;
}