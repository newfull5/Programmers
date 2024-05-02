def solution(data, col, row_begin, row_end):    
    data = sorted(data, key = lambda x: x[0], reverse=True)
    data = sorted(data, key = lambda x: x[col-1])
    s_i = [sum([d % (i+1) for d in data[i]]) for i in range(row_begin-1, row_end)]
    answer = s_i.pop()
    
    for num in s_i:
        answer = answer^num
        
    return answer
