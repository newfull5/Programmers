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
            
        
