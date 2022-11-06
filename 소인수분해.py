def divide(num, n):
    while num % n == 0:
        num = num // n
    return num

def solution(n):
    answer = []
    for num in range(2,10000):
        if n < num:
            break
        if n % num == 0:
            n = divide(n, num)
            answer.append(num)
    return answer
