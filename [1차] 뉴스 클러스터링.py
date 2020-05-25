def solution(str1, str2):
    set1 = []
    set2 = []
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    for i in range(len(str1)-1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i+1]) <= 90:
            set1.append(str1[i]+str1[i+1])

    for i in range(len(str2)-1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i+1]) <= 90:
            set2.append(str2[i]+str2[i+1])
            
    if not set1 and not set2:
        return 65536
            
    cnt = 0
    length = len(set1+set2)

    while set1 and set2:
        p = set1.pop()
        for st in set2:
            if p == st:
                cnt += 1
                set2.remove(st)
                break
                
    return int((cnt / (length - cnt)) * 65536)
