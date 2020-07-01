#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    
    
    
    char* answer = (char*)malloc(strlen(s) + 1);
    bool isodd = true;
    
    strcpy(answer, s);
    
    for (int i = 0; i < strlen(s); i++){
        if (answer[i] == ' '){
            isodd = true;
            continue;
        }
        answer[i] = isodd ? toupper(answer[i]) : tolower(answer[i]);
        isodd = !isodd;
    }
    return answer;
}
