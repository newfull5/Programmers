def go_lower(storey, cnt):
    mod = storey % 10
    cnt += mod
    return storey//10, cnt

def go_upper(storey, cnt):
    mod = storey % 10
    cnt += 10 - mod
    return (storey//10)+1, cnt

def solution(storey):
    queue = [(storey, 0)]
    answer = []
    
    while queue:
        next_queue = []
        
        for storey, cnt in queue:
            if storey == 0 or storey == 1:
                answer.append(cnt+storey)
                continue
            
            next_queue.append(go_upper(storey, cnt))
            next_queue.append(go_lower(storey, cnt))
            
        queue = next_queue
        
    return min(answer)
