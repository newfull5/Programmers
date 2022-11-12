'''
def solution(nums):
    arr = []
    cnt = 0
    answer = []
    
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                arr.append(nums[i]+nums[j]+nums[k])
                
    
    for num in arr:
        for i in range(1,num+1):
            if num%i == 0:
                cnt = cnt + 1
            if i == num and cnt == 2:
                answer.append(num)
        cnt = 0
        
    return len(answer)
'''
'''
#2020.03.04
#5달전 나의 풀이를 살펴보니 기분이 묘하다. 그땐 itertools도 몰라서 수작업으로 구현하고 일일이 비교하며 답을 구했다.
#쉬운 작업이 아니었을텐데 끝까지 구현하여 답을 맞추었었구나, 대견하기도 하다.
from itertools import combinations

def solution(nums):
    arr = list(combinations(sorted(nums),3))
    cnt = 0
    prime = [2]

    for i in range(3, sum(arr[-1])+1):
        prime.append(i)
        for j in range(0,len(prime)-1):
            if i % prime[j] == 0:
                prime.pop()
                break

    for num in arr:
        if sum(num) in prime:
            cnt += 1
            
    return cnt
'''
#2022.11.12
from itertools import combinations

def check_prime(num):
    if num % 2 == 0:
        return False
    for n in range(3,num,2):
        if num % n == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for val in combinations(nums, 3):
        if check_prime(sum(val)):
            answer += 1
            
    return answer
