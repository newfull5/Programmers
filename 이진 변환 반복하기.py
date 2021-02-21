def solution(s):
    
    def Recul(s,count,times):
        if s == '1':
            return [times, count]

        count += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        return Recul(s,count,times+1)

    return Recul(s,0,0)
