def solution(string):
    cnt = 0
    answer = 0
    
    while string:
        for i, v in enumerate(string):
            if i == 0:
                start_char = v
                cnt += 1
                continue

            if v == start_char:
                cnt += 1

            if (i+1)/2 == cnt:
                answer += 1
                string = string[i+1:]
                cnt = 0
                break
        else:
            return answer+1
        
    return answer
