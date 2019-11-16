def solution(stock, dates, supplies, k):
    s = 0
    cnt = 0
    posida = []
    
    while stock < k:
        posida = []
        for i in range(0, len(dates)):
            if stock >= dates[i]:
                posida.append(supplies[i])

        s = max(posida)
        dates.remove(dates[posida.index(s)])
        supplies.remove(s)

        stock = stock + s
        cnt += 1
    
    return cnt
