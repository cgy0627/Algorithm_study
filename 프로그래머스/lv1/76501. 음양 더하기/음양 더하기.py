def solution(absolutes, signs):
    res = 0
    new_signs = [1 if sign == True else -1 for sign in signs]
    for i in range(len(absolutes)):
        res += absolutes[i] * new_signs[i]
    
    return res