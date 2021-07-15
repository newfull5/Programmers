def solution(gems):
    size = len(set(gems)) 
    dic = {gems[0]:1}
    length = len(gems)

    left, right = 0,0

    answer = (len(gems), [0,len(gems)])

    while (left < length and right < length): 
        if len(dic) == size:
            if right - left < answer[0]:
                answer = (right-left, [left, right])

            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1

        else:
            right += 1
            if right >= length:
                break
            if gems[right] in dic.keys():
                dic[gems[right]] += 1
            else:
                dic[gems[right]] = 1

    answer = answer[-1]
    return [answer[0]+1, answer[1]+1]
