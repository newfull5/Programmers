def solution(n):
    answer = [[0]*i for i in range(1, n+1)]    
    cnt = 1
    x = 0
    y = 0
    direction = 'd'
    
    for num in range(n, 0, -1):
        for i in range(num):
            answer[x][y] = cnt
            cnt += 1
            
            if i == num-1:
                if direction == 'd':
                    direction = 'r'
                elif direction == 'r':
                    direction = 'u'
                elif direction == 'u':
                    direction = 'd'
                    
            if direction == 'd':
                x +=1
            elif direction == 'r':
                y += 1
            elif direction == 'u':
                x -= 1
                y -= 1
        
        
    return sum(answer, [])
