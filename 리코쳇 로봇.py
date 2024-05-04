'''
import numpy as np

def solution(board):
    answer = []
    board = np.array([list(b) for b in board])
    height = len(board)
    width = len(board[0])
    
    r,c = np.where(board == 'R')
    start = [int(r), int(c)]
    
    r,c = np.where(board == 'G')
    goal = [int(r), int(c)]
    
    def dfs(start, visited, cnt):
        if start in visited:
            return
        if start == goal:
            answer.append(cnt-1)
            return
        
        visited.append(start)
        start_r, start_c = start
        possible_path = []
        
        # left 
        if start_c != 0:
            for c in range(start_c, -1, -1):
                if board[start_r, c] == 'D':
                    possible_path.append([start_r, c+1])
                    break
            else:
                possible_path.append([start_r, 0])
                
        # right
        if start_c != width-1:
            for c in range(start_c, width):
                if board[start_r, c] == 'D':
                    possible_path.append([start_r, c-1])
                    break
            else:
                possible_path.append([start_r, width-1])
                
        # up
        if start_r != 0:
            for r in range(start_r, -1, -1):
                if board[r, start_c] == 'D':
                    possible_path.append([r+1, start_c])
                    break
            else:
                possible_path.append([0, start_c])
        
        # down
        if start_r != height-1:
            for r in range(start_r, height):
                if board[r, start_c] == 'D':
                    possible_path.append([r-1, start_c])
                    break
            else:
                possible_path.append([height-1, start_c])
        
        for path in possible_path:
            dfs(path, visited, cnt+1)
            
            
    dfs(start, [], 0)
    
    if not answer:
        return -1
    return min(answer)
'''
