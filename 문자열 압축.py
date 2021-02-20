def solution(s):
    result = len(s)

    for length in range(1, 1 + len(s) // 2):
        answer = ''
        prev = s[:length]    
        cnt = 1
        for i in range(length, len(s)+length, length):
            current = s[i:i+length]

            if current == prev:
                cnt += 1
            else:
                if cnt == 1:
                    answer += prev
                else:
                    answer += (str(cnt) + prev)
                    cnt = 1

            prev = current

        result = min(result, len(answer))

    return result
