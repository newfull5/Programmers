def solution(N, stages):
    length = len(stages)
    arr = []
    answer = []

    for i in range(1,N+1):
        if length == 0:
            arr.append((i,0))
            continue
        arr.append((i,stages.count(i)/length))
        length = length - stages.count(i)


    arr = sorted(arr, key=lambda arr: arr[1],reverse = True)

    for i in range(0, len(arr)):
        answer.append(arr[i][0])
        
    return answer
