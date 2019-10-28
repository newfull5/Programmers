def solution(array, commands):
    answer = []
    arr = []
    
    for t in range(0, len(commands)):
        i = commands[t][0]
        j = commands[t][1]
        k = commands[t][2]

        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])

    return answer
