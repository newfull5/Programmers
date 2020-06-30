#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int solution(int n) {
    int a = 3;
    int b = 4;
    int sum = 0;
    
    for (int i = 0; i < 10; i++){
        if (n < (int)pow((double)10, (double)i)){
            for (int j = i+1; j >= 0; j--){
                int temp = (int)pow((double)10, (double)j);
                sum += n / temp;
                n = n % temp;
            }
        }
    }
    return sum;    
}
