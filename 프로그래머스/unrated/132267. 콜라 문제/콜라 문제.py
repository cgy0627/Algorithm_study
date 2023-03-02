def solution(a, b, n):
    count = 0
    while n >= a:
        count += n//a * b
        n = (n % a) + (n // a * b)
    
    return count