def solution(elements):
    answer = set()
    max_window_size = len(elements)
    elements = elements + elements
    
    for win_size in range(1,max_window_size+1):
        for start_idx in range(max_window_size):
            answer.add(sum(elements[start_idx:start_idx+win_size]))
            
    return len(answer)
