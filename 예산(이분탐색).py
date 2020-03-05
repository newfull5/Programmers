def solution(budgets, M):
    
    def confirm(answer):
        nonlocal budgets
        temp = 0
        for num in budgets:
            if num < answer:
                temp += num
            else:
                temp += answer
        return temp

    a, b = 0, max(budgets)
    
    while b>=a:
        mid = (a+b)//2
        if confirm(mid) > M:
            b = mid-1
        else:
            answer = mid
            a = mid+1
    return answer
