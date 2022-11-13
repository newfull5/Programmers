"""
def solution(s):
    
    def Recul(s,count,times):
        if s == '1':
            return [times, count]

        count += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        return Recul(s,count,times+1)

    return Recul(s,0,0)
"""
#2022.11.13
def dfs(s,times,cnt):
    cnt += s.count('0')
    times += 1
    s = s.replace('0','')
    
    if s == '1':
        return [times, cnt]
    
    return dfs(bin(len(s))[2:], times, cnt)

def solution(s):
    return dfs(s, 0, 0)
