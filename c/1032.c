#include <stdio.h>
#include <stdlib.h>

char *modify(char *file, int index){
    *(file+index) = '?';
    return file;
}

int main(){

    int n, i, j;
    char **files = NULL;

    scanf("%d", &n);

    files = malloc(n * sizeof(char*));

    for(int i=0;i<n;i++){
        files[i] = malloc(51 * sizeof(char));
        scanf("%s", files[i]);
    }

    char *result = files[0];

    if(n != 1){
        for(int i=1;i<n;i++){
            j = 0;

            while(files[i][j] != '\0'){
                if(result[j] != files[i][j] && result[j] != '?'){
                    result = modify(result, j);
                }
                j++;
            }
        }
    }

    printf("%s\n", files[0]);

    return 0;
}
