def solution(rsp):
    answer = ''
    for v in rsp:
        if v == '2':
            answer += '0'
        if v == '0':
            answer += '5'
        if v == '5':
            answer += '2'
            
    return answer
