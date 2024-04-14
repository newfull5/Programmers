from collections import deque, Counter

def solution(weights):
    weights = deque(sorted(weights))
    diction = Counter(weights)
    answer = 0
    
    while weights:
        weight = weights.popleft()
        diction[weight] -= 1
        for num in [weight, weight*3/2, weight*2, weight*2/3, weight*4/3, weight*3/4]:
            answer += diction[num]
                
    return answer
