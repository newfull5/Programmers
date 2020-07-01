#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    int answer = x;
    int sum = 0;
    while (x > 0){
        sum += x % 10;
        x /= 10;
    }
    return (answer % sum == 0);
}
