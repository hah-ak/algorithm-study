def solution(board):
    
    size = 1
    row_size, column_size = len(board), len(board[0])
    row = 0
    while row + size < len(board):

        for c in range(column_size+1-size):
            if c+size > column_size:
                break
            if 0 not in board[row][c:c+size]:
                row_check = True
                while c+1+size <= column_size and row + size < row_size:
                    for r in range(row,row+size+1):
                        if 0 not in board[row][c+size:c+1+size]:
                            None
                        else:
                            row_check = False
                            break
                    if row_check:
                        if 0 not in board[row+size][c:c+1+size]:
                                size += 1
                        else:
                            break
        row += 1
    return size ** 2


# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))