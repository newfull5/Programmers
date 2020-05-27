import re

def solution(files):
    q = re.compile('\d+')
    concat = []
    
    for file in files:
        span = q.search(file).span()
        a = file[:span[0]].upper()
        b = int(file[span[0]:span[1]])

        concat.append((a,b,file))
        
    concat = sorted(concat, key = lambda x: x[1])
    concat = sorted(concat, key = lambda x: x[0])
    
    return [c for a,b,c in concat]
