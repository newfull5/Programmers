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
