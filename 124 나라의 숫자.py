#역시 재귀는 어렵다.

def solution(a): 
    answer = ''
    def div(a):
        nonlocal answer
        if a == 0:
            return answer[::-1]
        if a % 3 == 0:
            answer += '4'
            return div(a//3 - 1)
        if a % 3 == 1:
            answer += '1'
            return div(a//3)
        if a % 3 == 2:
            answer += '2'
            return div(a//3)
    return div(a)
