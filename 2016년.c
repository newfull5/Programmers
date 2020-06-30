#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    int days[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31};
    int dydlf[7] = {"THU","FRI","SAT","SUN","MON","TUE","WED"};
    int daysum = 0;
    
    for (int i = 0; i < a; i++){
        daysum += days[i];
    }
    daysum += b;
    
    return dydlf[daysum % 7];
}
