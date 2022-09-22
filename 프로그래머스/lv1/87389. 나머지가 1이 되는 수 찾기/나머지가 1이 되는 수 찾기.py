def solution(n):
    for i in range(2, n//2):
        if n % i == 1:
            return i
    
    return n-1