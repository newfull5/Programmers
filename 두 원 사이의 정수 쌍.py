def solution(r1, r2):
    possible = []
    r1_cnt, r2_cnt = 0, 0
    
    for x in range(1, r1+1):
        num = (r1**2 - x**2) ** (1/2)
        if num == int(num):
            r1_cnt += int(num)
        else:
            r1_cnt += int(num)+1
        
    for x in range(1, r2+1):
        r2_cnt += int((r2**2 - x**2)**(1/2)) + 1
                
    r2_cnt = r2_cnt*4 + 1
    r1_cnt = r1_cnt*4 + 1
    
    return r2_cnt - r1_cnt
