def solution(board, k):
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                ans += board[i][j]
    
    return ans