'''
def solution(sequence, k):
    answers = []
    sum = 0
    l = 0
    r = -1
    
    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum == k:
            answers.append([l, r])
    
    answers.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answers[0]
'''
def solution(sequence, k):
    answer = [0,0]
    answer_len = 1_000_000
    
    for left in range(len(sequence)):
        for right in range(left+1, len(sequence)+1):
            window_size = right - left
            
            if window_size >= answer_len:
                break
            
            if sum(sequence[left:right]) < k:
                continue
                
            elif sum(sequence[left:right]) > k:
                break
                
            elif sum(sequence[left:right]) == k:
                if window_size == 1:
                    return [left, right-1]
                
                answer = [left, right-1]
                answer_len = right-left
                
    return answer
