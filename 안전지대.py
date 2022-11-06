def marking(i, j, board):
    max_length = len(board)-1
    if i != 0:
        board[i-1][j] = 1 # up
    if i != 0 and j != 0:
        board[i-1][j-1] = 1 # up left
    if i != 0 and j != max_length:
        board[i-1][j+1] = 1 # up right
    if j != 0:
        board[i][j-1] = 1 # left
    if j != max_length:
        board[i][j+1] = 1 # right
    if i != max_length and j != 0:
        board[i+1][j-1] = 1 # left down
    if i != max_length and j != max_length:
        board[i+1][j+1] = 1 # right down
    if i != max_length:
        board[i+1][j] = 1 # down
    board[i][j] = 1
    return board

def solution(board):
    answer = [[0]*len(board) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                answer = marking(i,j,answer)
    return len(board)**2 - sum(sum(answer, []))
