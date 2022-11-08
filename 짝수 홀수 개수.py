def solution(num_list):
    answer = 0
    for num in num_list:
        if num % 2 == 0:
            answer += 1
    return [answer, len(num_list)-answer]
