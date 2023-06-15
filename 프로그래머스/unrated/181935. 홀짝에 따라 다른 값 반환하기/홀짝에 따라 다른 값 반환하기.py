def solution(n):
    return sum(range(1,n+1,2)) if n % 2 == 1 else sum(map(lambda x: x**2, range(0,n+1,2)))