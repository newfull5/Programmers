#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int n) {
    char* answer = (char*)malloc(n*3 + 1);
    if (n == 1){
        return "수";
    }
    strcpy(answer, "수박");
    for(int i = 2; i <= n/2; i++){
        strcat(answer, "수박");
    }
    if (n%2){
        strcat(answer, "수");
    }
    
    return answer;
}
