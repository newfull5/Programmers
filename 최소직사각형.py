"""
def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = [min(sizes[i]), max(sizes[i])]

    return max([a for a,b in sizes])* max([b for a,b in sizes])

"""
#2022.11.08
def solution(sizes):
    sizes = [sorted(li) for li in sizes]
    max_w, max_h = 0, 0
    for w,h in sizes:
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
            
    return max_h * max_w
