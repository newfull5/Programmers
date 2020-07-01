#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
//0 = 48 1 = 49 9 = 57
bool solution(const char* s) {
    if (strlen(s) != 4 && strlen(s) != 6) {
        return false;
    }
    
    for (int i = 0; i < strlen(s); i++){
        if (s[i] > 57){
            return false;
        }
    }
    
    return true;
}
