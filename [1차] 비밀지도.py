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
