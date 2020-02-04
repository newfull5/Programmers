def solution(skill, skill_trees):
    answer = []
    for i in range(0, len(skill)):
        answer.append(skill[:i])
    answer.append(skill)

    cnt = 0
    for arr in skill_trees:
        temp = []
        for i in range(0,len(arr)):
            if arr[i] in list(skill):
                temp.append(arr[i])
                print(temp)
        if ''.join(temp) in answer:
            cnt += 1
            
    return cnt
