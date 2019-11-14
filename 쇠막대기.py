def solution(arrangement):
    cnt = 0
    arrangement = list(arrangement.replace('()','r'))
    for i in range(0, len(arrangement)):
        j = 0
        if arrangement[i] == ')':
            while True:
                j += 1
                if arrangement[:i][-j] == '(':
                    arrangement[i] = 'a'
                    arrangement[i-j] = 'a'
                    cnt += (arrangement[i-j:i].count('r')+1)
                    break


        if not '(' in arrangement:
            break
            
    return cnt
