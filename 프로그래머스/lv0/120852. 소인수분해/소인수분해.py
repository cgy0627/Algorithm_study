def solution(n):
    ans = set()
    d = 2
    while d <= n:
        if n % d == 0:
            ans.add(d)
            n = n // d
        else:
            d += 1
    return sorted(list(ans))