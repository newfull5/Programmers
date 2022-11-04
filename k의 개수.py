def solution(i, j, k):
    bar = ''
    for num in range(i,j+1):
        bar += str(num)
    return bar.count(str(k))
