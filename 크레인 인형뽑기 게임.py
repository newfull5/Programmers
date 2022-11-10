"""
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
"""
import numpy as np
from collections import deque


def solution(board, moves):
    stack = [-1, 0]
    answer = 0

    board = np.rot90(np.array(board)).tolist()
    board = [deque(li) for li in board][::-1]

    for idx in moves:
        if not board[idx - 1]:
            continue

        while board[idx - 1][0] == 0:
            board[idx - 1].popleft()

        stack.append(board[idx - 1].popleft())

        while stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2

    return answer
