def solution(common):
    a,b,c = common[:3]
    
    if a-b == b-c:
        return common[-1] + (b-a)
    else:
        return common[-1] * (b/a)
