def solution(n):
    num = 1
    while(True):
        if num * num == n:
            return 1
        elif num * num > n:
            return 2
        num += 1