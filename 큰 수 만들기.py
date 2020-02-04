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
