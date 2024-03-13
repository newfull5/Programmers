def get_divisor(num):
    if num == 1:
        return 1
    
    cnt = 0
    for n in range(1, int(num**(1/2)+1)):
        if num % n == 0:
            cnt += 1

    if num**(1/2) == int(num**(1/2)):
        return (cnt*2)-1
    return cnt*2

def solution(number, limit, power):
    answer = 0

    for num in range(1, number+1):
        divisor = get_divisor(num)
        if divisor > limit:
            answer += power
        else:
            answer += divisor
            
    return answer
