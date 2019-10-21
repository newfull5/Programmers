def solution(n, words):
    wrong = 0
    for i in range(0, len(words)-1):
        if words[i][-1] != words[i+1][0]:
            wrong = i+2
            break

    for i in range(0, len(words)-1):
        for j in range(i+1, len(words)):
            if words[i] == words[j]:
                wrong = j+1
                break
    
    if wrong == 0:
        return [0,0]
    if wrong%n == 0:
        return [n,wrong//n]
    else:
        return [wrong%n,(wrong//n)+1]
