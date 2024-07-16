'''
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
'''
def solution(gems):
    num_kinds = len(set(gems))
    answer = [0, float('inf')]
    
    def check_include_all(l,r):
        if len(set(gems[l:r])) == num_kinds:
            return True
        return False
    
    
    for left in range(0, len(gems)):
        for right in range(left+1, len(gems)+1):
            
            if right - left >= answer[1]-answer[0]:
                break
                
            if check_include_all(left, right):
                while check_include_all(left, right):
                    left += 1
                answer = [left, right]
        
    return answer
