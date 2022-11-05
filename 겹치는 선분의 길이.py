def solution(lines):
    set1, set2, set3 = [set(range(min(line), max(line))) for line in lines]
    return len((set1 & set2) | (set1 & set3) | (set2 & set3))
