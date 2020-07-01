#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num) {
    long long answer = num;
    for (int i = 0; i < 500; i++){
        if (answer == 1){
            return i;
        }
        answer = (answer % 2 == 0) ? answer/2 : (answer*3) + 1;
    }
    printf("%d", answer);
    return -1;
    
}
