def solution(order):
    answer = 0
    max_l = len(order)

    sub = []
    l = 1
    o = 0
    while order and l <= max_l + 1 and o < max_l:

        if l == order[o]:
            while l == order[o]:
                o += 1
                l += 1
                answer+=1
            continue
        elif sub and sub[-1] == order[o]:
            while sub and sub[-1] == order[o]:
                sub.pop(-1)
                o += 1
                answer +=1
            continue
        elif o >= max_l  or order[o] < l :
            return answer
        elif l < max_l :
            sub.append(l)
            l += 1
            continue
        else:
            return answer
    return answer
