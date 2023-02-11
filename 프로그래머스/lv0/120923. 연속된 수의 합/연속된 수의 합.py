def solution(num, total):
    mid = total // num
    side = num // 2
    
    if num % 2 == 0:
        return [i for i in range(mid-side+1, mid+side+1)]
    else:
        return [i for i in range(mid-side, mid+side+1)]