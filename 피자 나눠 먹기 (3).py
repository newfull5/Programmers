def solution(slice, n):
    for num in range(1, n+1):
        if num*slice >= n:
            return num
