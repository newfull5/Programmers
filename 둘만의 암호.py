def shift_char(num, skip, index):
    for _ in range(index):
        num += 1
        if num > 122:
            num = (num % 123) + 97
        while True:
            if num in skip:
                num += 1
                if num > 122:
                    num = (num % 123) + 97
            if num not in skip:
                break
    if num > 122:
        num = (num % 123) + 97

    return num

def solution(s, skip, index):
    s = list(map(ord, s))
    skip = list(map(ord, skip))
    return ''.join([chr(shift_char(v, skip, index)) for v in s])
