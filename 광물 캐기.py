from collections import deque

def calc_fatigue(rhr, target):
    if rhr == 0:
        return 1
    if rhr == 1:
        if target == 'diamond':
            return 5
        return 1
    if rhr == 2:
        if target == 'diamond':
            return 25
        if target == 'iron':
            return 5
        return 1

def solution(picks, minerals):
    answer = []
    
    def dfs(minerals, picks, rhr, cnt):
        if picks[rhr] == 0:
            return
        picks[rhr] -= 1
        
        if not minerals:
            answer.append(cnt)
            return
        
        targets = minerals[:5]
        minerals = minerals[5:]
        
        fatigue = sum([calc_fatigue(rhr,target) for target in targets])
        
        if sum(picks) == 0:
            answer.append(cnt+fatigue)
            return
        dfs(minerals, picks, 0, cnt+fatigue)
        dfs(minerals, picks, 1, cnt+fatigue)
        dfs(minerals, picks, 2, cnt+fatigue)
        
    dfs(minerals, picks, 0, 0)
    dfs(minerals, picks, 1, 0)
    dfs(minerals, picks, 2, 0)
    
    return min(answer)
