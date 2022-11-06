def solution(numbers, k):
    numbers = numbers * 1000
    return numbers[k*2-2]
