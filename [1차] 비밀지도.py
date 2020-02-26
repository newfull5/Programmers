'''
def solution(n, arr1, arr2):
    answer1 = []
    answer2 = []
    answer = []

    for arr in arr1:
        if len(bin(arr)[2:]) != n:
            answer1.append((n - len(bin(arr)[2:]))*'0' + bin(arr)[2:])
        else:
            answer1.append(bin(arr)[2:])

    for arr in arr2:
        if len(bin(arr)[2:]) != n:
            answer2.append((n - len(bin(arr)[2:]))*'0' + bin(arr)[2:])
        else:
            answer2.append(bin(arr)[2:])

    for i in range(0, n):
        temp = ''
        for j in range(0,n):
            if answer1[i][j] == '1' or answer2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '

        answer.append(temp)
    return answer
'''
# 2020.02.26
# 20일전 풀이에서 조금도 달라진게 없다. 풀이가 하나밖에 없는 문제인건가? 아니면 성장하지 못한 것인가?
def solution(n, arr1, arr2):
    ar1 = []
    ar2 = []
    answer = []
    
    for num in arr1:
        if len(bin(num)[2:]) != n:
            ar1.append('0'*(n - len(bin(num)[2:])) + bin(num)[2:])
        else:
            ar1.append(bin(num)[2:])
            
    for num in arr2:
        if len(bin(num)[2:]) != n:
            ar2.append('0'*(n - len(bin(num)[2:])) + bin(num)[2:])
        else:
            ar2.append(bin(num)[2:])
            
    for i in range(0, n):
        string = ''
        for j in range(0, n):
            if ar1[i][j] == '1' or ar2[i][j] == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)
        
    return answer
