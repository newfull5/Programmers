#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool solution(const char* s) {
    int length = strlen(s);
    int answer = 0;
    
    for (int i = 0; i < length; i++){
        answer += (s[i] == '(') ? 1 : -1;
        if (answer == -1) return false;
    }
    return answer == 0;
}
