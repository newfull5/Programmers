def f(x):
    if x % 2 == 0:
        return x+1
    
    x = '0' + bin(x)[2:]
    idx = x.rfind('0')
    x = list(x)
    x[idx] = '1'
    x[idx+1] = '0'
    x = ''.join(x)

    return int(x, base = 2)

def solution(numbers):
    return [f(x) for x in numbers]
