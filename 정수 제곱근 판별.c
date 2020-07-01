#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

long long solution(long long n) {
    long long answer = 0;
    double a = pow((double) n, (double) 0.5);
    if (a == (int)a){
        a++;
        return a*a;
    }

    return -1;
}
