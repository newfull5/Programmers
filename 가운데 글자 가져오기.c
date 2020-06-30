#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* s) {
    char* answer = (char*)malloc(1);
    int k = strlen(s);
    
    char arr[k];
    char arrs[3];
    
    strcpy(arr, s);
    
    if (k % 2 == 0){
        k = k/2;
        arrs[0] = arr[k-1];
        arrs[1] = arr[k];
    }
    else{
        k = k/2;
        arrs[0] = arr[k];
    }
    
    strcpy(answer, arrs);
    return answer;
}
