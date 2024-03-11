import heapq

def solution(k, scores):
    heap = []
    answer = []

    for i, score in enumerate(scores):
        if i < k:
            heapq.heappush(heap, score)
            answer.append(heap[0])
            continue

        elif heap[0] < score:
            heapq.heappop(heap)
            heapq.heappush(heap, score)
            
        answer.append(heap[0])
                
    return answer
