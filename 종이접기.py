def solution(n):
    if n == 1:
        return [0]
    
    before = '0'
    for _ in range(n-1):
        answer = []
        for i in range(0,len(before)):
            if i % 2 == 0 :
                answer.append('0')
                answer.append(before[i])
            else:
                answer.append('1')
                answer.append(before[i])
        answer.append('1')

        before = "".join(answer)[:]
        
    return list(map(int, answer))
