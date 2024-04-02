'''
def cycle(number, cnt):
    if cnt == 0:
        return number
    
    for i in range(0, len(number)-1):
        if number[i] < number[i+1]:
            number = number[:i] + number[i+1:]
            cnt -= 1
            return cycle(number, cnt)
    
    number = list(number)
    number = number.remove(min(number))
    return cycle(''.join(number),cnt)

def solution(number, k):
    temp_index = number[:k].index(max(list(number[:k])))
    number = number[temp_index:]
    k = k - temp_index
    
    return cycle(number, k)
'''

'''
def solution(number, k):
    length = len(number)
    m = 0
    for cnt in range(k):
        for idx in range(m, length-1):
            if number[idx] < number[idx+1]:
                number = number[:idx] + number[idx+1:]
                length -= 1
                if idx > 0:
                    m = idx-1
                break
            else:
                number = number[:length-k+cnt]
                break
    return "".join([str(i) for i in number])
'''
'''
def solution(number, k):
    a = 0
    while k != 0:
        for i in range(a, len(number)-1):
            if number[i] < number[i+1]:
                number = number.replace(number[i],'',1)
                k -= 1
                if i == 0:
                    a = i
                else:
                    a = i-1
                break
            if i == len(number):
                number = number[:-1]
    return number
'''
#2024.04.02
def solution(number, k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k != 0:
        return ''.join(stack)[:-k]
    return ''.join(stack)
