"""
#2020.02.25
def solution(genres, plays):
    if len(genres) == 1:
        return [0]
        
    stack = []
    maxplay = []
    answer = []
    for i in range(0, len(genres)):
        stack.append([i,genres[i],plays[i]])

    for kind in set(genres):
        cnt = 0
        for num in stack:
            if num[1] == kind:
                cnt += num[2]
        maxplay.append([kind,cnt])

    maxplay = sorted(maxplay, reverse = True, key = lambda a: a[1])

    stack = sorted(stack, key = lambda a: a[2], reverse = True)
    stack = sorted(stack, key = lambda a: a[1], reverse = True)

    for kind in maxplay:
        for i in range(0, len(stack)-1):
            if stack[i][1] == kind[0] and stack[i+1][1] == kind[0]:
                answer.append(stack[i][0])
                answer.append(stack[i+1][0])
                break
            if stack[i][1] == kind[0] and stack[i+1][1] != kind[0]:
                answer.append(stack[i][0])
                break
                
    if maxplay[-1][0] == stack[-1][1] and maxplay[-1][0] != stack[-2][1]:
        answer.append(stack[-1][0])  
        
    return answer
"""
#2021.01.25
def solution(genres, plays):
    max_gernes = {gen:0 for gen in set(genres)}

    answer = []

    for i in range(len(genres)):
        max_gernes[genres[i]] = max_gernes[genres[i]] + plays[i]

    max_gernes = sorted(max_gernes.items(), key = lambda x: x[-1])

    while max_gernes:
        gen = max_gernes.pop()[0]
        temp_arr = []

        for i in range(len(genres)):
            if genres[i] == gen:
                temp_arr.append((i,plays[i]))

        temp_arr = sorted(temp_arr, key = lambda x: x[0], reverse=True)
        temp_arr = sorted(temp_arr, key = lambda x: x[1])

        if len(temp_arr) == 1:
            answer += [temp_arr.pop()[0]]
        else:
            answer += [temp_arr.pop()[0], temp_arr.pop()[0]]
            
    return answer
