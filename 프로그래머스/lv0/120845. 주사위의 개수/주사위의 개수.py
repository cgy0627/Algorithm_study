def solution(box, n):
    ans = 1
    for b in box:
        ans *= b//n
    return ans