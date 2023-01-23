def solution(keyinput, board):
    ans = [0,0]
    
    for arrow in keyinput:
        if (arrow == "left") & (ans[0] > -board[0]//2 + 1):
            ans[0] -= 1
        elif (arrow == "right") & (ans[0] < board[0]//2):
            ans[0] += 1
        elif (arrow == "down") & (ans[1] > -board[1]//2 + 1):
            ans[1] -= 1
        elif (arrow == "up") & (ans[1] < board[1]//2):
            ans[1] += 1
    
    return ans