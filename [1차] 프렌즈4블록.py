'''
def Square(board):
    a = len(board)-1
    data = []
    for i in range(0, a):
        for j in range(0, min(len(board[i]), len(board[i+1]))-1):
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                data.append((i,j))
                data.append((i,j+1))
                data.append((i+1,j))
                data.append((i+1,j+1))
    return data

def solution(m, n, board):
    board = list(map(lambda x: list(x),board))
    board = list(map(list, zip(*board)))
    board = list(map(lambda x: x[::-1],board))
    
    while True:
        data = Square(board)
        data = sorted(list(set(data)),reverse=True)
        
        if not data:
            return m*n-len(sum(board,[]))
        
        for a,b in data:
            del board[a][b]
'''
#2022.11.29
import numpy as np

def check_window(w,h,board):
    if board[h, w] == board[h, w+1] == board[h+1, w] == board[h+1, w+1]:
        if board[h, w] == '1':
            return False
        return True
    return False

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    board = np.array(board)
    
    answer = 0
    while True:
        redun_idx = set()
        for w in range(n-1):
            for h in range(m-1):
                if check_window(w,h,board):
                    redun_idx.add((h,w))
                    redun_idx.add((h,w+1))
                    redun_idx.add((h+1,w))
                    redun_idx.add((h+1,w+1))

        # Set vector '1'
        for h,w in redun_idx:
            board[h, w] = '1'

        # Shit vecotr down
        for w in range(n):
            cnt = np.count_nonzero(board[:, w] == '1')
            board[:, w] = np.array(['1']*cnt + board[:, w][board[:, w] != '1'].tolist())
        # Count the number of '1'
        if answer == np.count_nonzero(board == '1'):
            return answer
        answer = np.count_nonzero(board == '1')
