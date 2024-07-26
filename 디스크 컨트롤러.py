from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    len_jobs = len(jobs)
    current_time = 0
    jobs = deque(sorted(jobs, key = lambda x: x[0]))
    heap = []
    complete = []
    
    while len(complete) < len_jobs:
        while jobs:
            if jobs[0][0] <= current_time:
                start, end = jobs.popleft()
                heappush(heap, [end, start])
            else:
                break
        
        if heap:
            end, start = heappop(heap)
            current_time += end
            complete.append(current_time - start)
        else:
            current_time += 1
        
    return sum(complete) // len(complete)
