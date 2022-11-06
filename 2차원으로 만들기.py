from collections import deque

def solution(num_list, n):
    num_list = deque(num_list)
    answer = []
    
    while num_list:
        temp = []
        for _ in range(n):
            temp.append(num_list.popleft())
        answer.append(temp)
    
    return answer
