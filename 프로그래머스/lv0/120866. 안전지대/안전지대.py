def solution(board):
    length = len(board)
    for row in range(length):
        for col in range(length):
            if board[row][col] == 1:
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if (0 <= r < length) & (0 <= c < length):
                            board[r][c] = 'x' if board[r][c] != 1 else 1
    
    print(board)
    return sum(map(lambda x: x.count(0), board))