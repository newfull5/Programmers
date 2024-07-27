'''
def impossible(n, middle, times):
    return sum([middle // x for x in times]) < n

def solution(n, times):
    left, right = 1, max(times)*n
    while left < right:
        mid = (left + right) // 2
        print('mid :', mid)
        if impossible(n, mid, times):
            print('True')
            left = mid + 1
        else: 
            right = mid
            print('False')
    return left
'''

def solution(n, times):
    answer = 0
    left, right = 0, max(times)*n
    
    while left <= right:
        mid = (left + right)//2
        people = sum(mid//time for time in times)
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer
