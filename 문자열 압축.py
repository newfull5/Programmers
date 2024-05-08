'''
def solution(s):
    result = len(s)

    for length in range(1, 1 + len(s) // 2):
        answer = ''
        prev = s[:length]    
        cnt = 1
        for i in range(length, len(s)+length, length):
            current = s[i:i+length]

            if current == prev:
                cnt += 1
            else:
                if cnt == 1:
                    answer += prev
                else:
                    answer += (str(cnt) + prev)
                    cnt = 1

            prev = current

        result = min(result, len(answer))

    return result
'''
def solution(s):
    result=[]
    
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        for j in range(i, len(s)+i, i):
            
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                    
                tmp=s[j:j+i]
                cnt = 1
                
        result.append(len(b))
        

    return min(result)
