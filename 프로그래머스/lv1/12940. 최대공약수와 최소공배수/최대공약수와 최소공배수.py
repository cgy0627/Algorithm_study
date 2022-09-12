def solution(n, m):
    a, b = 0, 0
    if n > m: n, m = m, n
    
    for i in range(n, 0, -1):
        if (n % i == 0) & (m % i == 0):
            a = i
            break
    
    i = 1
    while True:
        if (m * i) % n == 0:
            b = m * i
            break
        i += 1
    
    return [a, b]