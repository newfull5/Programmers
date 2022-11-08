def solution(babbling):
    answer = 0
    for bab in babbling:
        if 'ayaaya' in bab:
            continue
        if 'yeye' in bab:
            continue
        if 'woowoo' in bab:
            continue
        if 'mama' in bab:
            continue
        if '' == bab.replace('aya',' ').replace('ye',' ').replace('woo',' ').replace('ma',' ').strip():
            answer += 1
    return answer
