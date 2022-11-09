"""
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer += [numbers[i]+numbers[j]]

    return sorted(list(set(answer)))
"""

"""
# 2020.10.07
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))
"""
#2022.11.09
from itertools import combinations

def solution(numbers):
    return sorted(list(set(sum(nums) for nums in combinations(numbers, 2))))
