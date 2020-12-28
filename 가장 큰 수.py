'''

def solution(numbers):
    hashh = []
    answer = ''

    maxlen = len(str(max(numbers)))

    for num in numbers:
        hashh.append([num,int(str(num)+((maxlen-len(str(num)))*str(num)[-1]))])

    hashh = sorted(hashh,key=lambda a: a[1], reverse = True)

    for has in hashh:
        answer += str(has[0])    

    return answer
    # 이게 왜 안되는지 모르겠다 아래랑 같은 방식인데 뭐지...
'''
"""
# 문자열의 대소 비교를 이용한 방법

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers = sorted(numbers,key=lambda a: a*3, reverse = True)
    return str(int(''.join(numbers)))
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    return (str(int(''.join(sorted(numbers, key = lambda x: x*3 , reverse = True)))))
    
