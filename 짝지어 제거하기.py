def solution(s):
    result = []
    for i in s:
        if not result:
            result.append(i)
        elif result[-1] == i:
            result.pop()
        else:
            result.append(i)
    return int(not bool(result))
