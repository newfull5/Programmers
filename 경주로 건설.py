from collections import deque


def solution(board):
    def move_left(row, col):
        if col == 0 or board[row][col-1] == 1:
            return
        return row, col-1

    def move_right(row, col):
        if col == len(board[0]) - 1 or board[row][col+1] == 1:
            return
        return row, col+1

    def move_up(row, col):
        if row == 0 or board[row-1][col] == 1:
            return
        return row-1, col

    def move_down(row, col):
        if row == len(board) - 1 or board[row+1][col] == 1:
            return
        return row+1, col

    visited = [[2_100_000_000]*len(board[0]) for _ in range(len(board))]

    row, col, cost = 0, 0, 0
    queue = deque([[row, col, cost, 'first_pass']])

    while queue:
        row, col, cost, before = queue.popleft()
        if visited[row][col] < cost:
            continue

        visited[row][col] = cost

        if move_left(row, col):
            if before == 'first_pass' or before == 'left':
                queue.append([row, col-1, cost+100, 'left'])
            else:
                queue.append([row, col-1, cost+600, 'left'])

        if move_right(row, col):
            if before == 'first_pass' or before == 'right':
                queue.append([row, col+1, cost+100, 'right'])
            else:
                queue.append([row, col+1, cost+600, 'right'])

        if move_up(row, col):
            if before == 'first_pass' or before == 'up':
                queue.append([row-1, col, cost+100, 'up'])
            else:
                queue.append([row-1, col, cost+600, 'up'])

        if move_down(row, col):
            if before == 'first_pass' or before == 'down':
                queue.append([row+1, col, cost+100, 'down'])
            else:
                queue.append([row+1, col, cost+600, 'down'])

    return visited[-1][-1]
