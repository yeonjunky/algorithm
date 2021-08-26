#include <stdio.h>

void check_palindrome(char* str, int len){
    int a = 0, b = len - 1;
    char isPalindrome = 1;

    for(int k=0;k<len/2;k++){
        if(str[a] == str[b]){
            a++;
            b--;
        }

        else {
            isPalindrome = 0;
            break;
        }
    }

    if(isPalindrome) printf("회문");
    else printf("아님");
    
}

int length_of_string(char*str){
    int count = 0;
    while (*str != '\0') {
        count++;
        str++;
    }

    return count;
}

int main(){
    char str[50] = "level";
    printf("%d\n", length_of_string(str));
    check_palindrome(str, length_of_string(str));
    return 0;
}