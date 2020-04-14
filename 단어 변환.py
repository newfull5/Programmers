def diffone(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
        if cnt == 2:
            break    
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    begin = [begin]
    answer = 0
    
    while words:
        for string in begin:
            temp = []
            for word in words:
                if diffone(string, word):
                    temp.append(word)
                    words.remove(word)
        answer += 1
        if target in temp:
            return answer
        begin = temp[:]
    return 0
