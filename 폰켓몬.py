'''
def solution(nums):
    
    num = set(nums)

    if len(num) >= len(nums)/2:
        return (len(nums)//2)
    else:
        return (len(num))
'''
#2020.03.07
def solution(nums):
    N = len(nums)//2
    nums = list(set(nums))
    
    if N >= len(nums):
        return len(nums)
    else:
        return N
