def solution(a, b, c):
    difflen = len(set([a, b, c]))
    if difflen == 1:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif difflen == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c