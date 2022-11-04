def solution(num_list, n):
    num_list = sorted(num_list, reverse=True)
    num_list = [(num, abs(num-n)) for num in num_list]
    num_list = sorted(num_list, key= lambda x: x[-1])
    return [num for num, _ in num_list]
