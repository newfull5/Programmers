def solution(board, moves):
    stack = []
    answer = 0
    
    for i in moves:
        for arr in board:
            if arr[i-1] != 0:
                print(arr[i-1])
                stack.append(str(arr[i-1])[:])
                arr[i-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break
                
    return answer
