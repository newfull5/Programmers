def solution(brown, red):
    brown = brown - 4
    brown = brown // 2
    temp = []
    for i in range(1, brown):
        if i * (brown - i) == red:
            return [(brown-i)+2,i+2]
