"""
def solution(arr):
    
    arr.remove(min(arr))
    
    if len(arr) == 0:
        return [-1]
    else:
        return arr
"""
#2022.11.12
def solution(arr):
    arr.remove(min(arr))
    if arr:
        return arr
    return [-1]
