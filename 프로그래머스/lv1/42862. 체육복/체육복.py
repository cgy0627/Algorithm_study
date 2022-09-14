def solution(n, lost, reserve):
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