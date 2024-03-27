def solution(x, y, n):
    queue = set([x])
    answer = 0
    
    while queue:
        if y in queue:
            return answer
        next_queue = set()
        
        for v in queue:
            if v*2 <= y:
                next_queue.add(v*2)
            if v*3 <= y:
                next_queue.add(v*3)
            if v+n <= y:
                next_queue.add(v+n)
                
        answer += 1
        queue = next_queue
    return -1
