#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int gcd(int a, int b){
    while (b > 0)
    {
        int tmp = a;
        a = b;
        b = tmp%b;
    }
    return a;
}

int solution(int arr[], size_t arr_len) {
    int answer = 1;
    for (int i = 0; i< arr_len; i++){
        answer = (answer*arr[i]) / gcd(answer ,arr[i]);
    }
    return answer;
}
