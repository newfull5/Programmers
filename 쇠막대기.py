'''
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

'''
#2020.02.07
#확실히 4달 전보다 성장하긴 했으나 시간 내에 풀 자신은 없다. 아직도 나는 한없이 작다.
def solution(arrangement):
    stack = []
    arrangement = arrangement.replace('()','r')
    
    cnt = 0
    for i in range(0, len(arrangement)):
        if arrangement[i] == '(':
            stack.append(i)
            
        if arrangement[i] == ')':
            cnt += arrangement[stack[-1]:i].count('r') + 1
            stack.pop()
    return cnt
