'''
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
'''
#힙을 사용하면 수행시간이 많이 줄어드는건 알겠습니다만... 언제 힙을 사용해야하는지 바로보고 판단할 자신이 없다.
#2020.03.01
import heapq

def solution(stock, dates, supplies, k):
    heap = []
    cnt = 0
    idx = 0
    while stock < k:
        for i in range(idx,len(supplies)):
            if dates[idx] > stock:
                break
            heapq.heappush(heap,(-supplies[i],supplies[i]))
            idx += 1
        stock += heapq.heappop(heap)[1]
        cnt += 1
        
    return cnt
