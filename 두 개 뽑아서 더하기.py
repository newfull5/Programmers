def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer += [numbers[i]+numbers[j]]

    return sorted(list(set(answer)))
