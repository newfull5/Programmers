def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = [min(sizes[i]), max(sizes[i])]

    return max([a for a,b in sizes])* max([b for a,b in sizes])
