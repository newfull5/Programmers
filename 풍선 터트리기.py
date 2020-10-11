from heapq import heapify, heappop, heappush

def solution(a):
    length = len(a)
    ballon = [(a[i],i) for i in range(length)]
    left, right = ballon[:1], ballon[1:]
    heapify(left)
    heapify(right)

    for i,b in enumerate(a[1:-1],1):
        if b == right[0][0]:
            while right[0][1] <= i:
                heappop(right)
        if b > left[0][0] and b > right[0][0]:
            length -= 1
        heappush(left, (b, i))
    return length
