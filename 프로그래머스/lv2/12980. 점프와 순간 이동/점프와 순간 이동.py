def solution(n):
    k = 1
    
    while n != 1:
        if n % 2 == 0:  # 짝수일 때
            n /= 2
        else:           # 홀수일 때
            n -= 1
            k += 1
    
    return k