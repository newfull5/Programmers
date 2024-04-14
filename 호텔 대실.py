def solution(book_time):
    num_rooms = 0
    answer = 0
    queue = []
    for start, end in book_time:
        a,b = start.split(':')
        queue.append([int(a) * 60 + int(b), 'start'])
        a,b = end.split(':')
        queue.append([int(a) * 60 + int(b) + 10, 'end'])
        
    queue = sorted(queue, key=lambda x:x[1])
    queue = sorted(queue, key=lambda x:x[0])
    
    for t, types in queue:
        if types == 'start':
            num_rooms += 1
        if types == 'end':
            num_rooms -= 1
            
        answer = max(num_rooms, answer)
        
    return answer
