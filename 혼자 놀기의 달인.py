def find_loop(cards, start_idx):
    answer = []
    
    while True:
        answer.append(start_idx)
        next_idx = cards[start_idx]
        start_idx = next_idx
        
        if start_idx in answer:
            break
            
    return answer

def solution(cards):
    answer = 0
    visited = []
    loops = []
    cards = [card-1 for card in cards]
    
    for num in range(len(cards)):
        if num in visited:
            continue
        
        loop = find_loop(cards, num)
        loops.append(loop)
        visited += loop
        
    loops = sorted(loops, key=lambda x:len(x))
    
    if len(loops) == 1:
        return 0
    
    return len(loops[-1]) * len(loops[-2])
