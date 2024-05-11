def get_sequence(k):
    answer = []
    cnt = 0
    n = -1
    while True:
        n += 1
        answer.append([cnt, k])
        if k == 1:
            return n, answer
        elif k % 2 == 1:
            k = k*3+1
        else:
            k = k // 2
            
        cnt += 1

def solution(k, ranges):
    answer = []
    n, seq = get_sequence(k)
    areas = []
    
    for i in range(len(seq)-1):
        _, y1 = seq[i]
        _, y2 = seq[i+1]
        areas.append(min([y1,y2]) + (abs(y1-y2) / 2))
        
    
    for rang in ranges:
        a,b = rang
        b = n-abs(b)
        
        if rang == [0,0]:
            answer.append(sum(areas))
            continue
            
        if a>b:
            answer.append(-1)
            continue
        
        answer.append(sum(areas[a:b]))
        
    return answer
