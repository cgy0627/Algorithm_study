def solution(n, lost, reserve):
#     reserve = set(reserve)

#     for size in [0, 1, -2]:
#         lost = set(map(lambda x : x+size, lost))
#         reserve, lost = reserve - lost, lost - reserve

#     return n - len(lost)

    lost1 = set(set(lost) - set(reserve))
    reserve1 = list(set(reserve) - set(lost))
    
    lost_len = len(lost1)
    for num in reserve1:
        lost1 -= {num-1}
        if len(lost1) == lost_len:
            lost1 -= {num+1}
            if len(lost1) != lost_len:
                lost_len -= 1
        else:
            lost_len -= 1
        
    return n - len(lost1)