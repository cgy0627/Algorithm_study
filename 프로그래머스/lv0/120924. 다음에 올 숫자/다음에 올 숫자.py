def solution(common):
    second = common[2] - common[1]
    first = common[1] - common[0]
    div = second // first if first != 0 else 0
    
    if div == 0:
        return common[-1]
    elif div == 1:
        return common[-1] + second
    else:
        return common[-1] * div