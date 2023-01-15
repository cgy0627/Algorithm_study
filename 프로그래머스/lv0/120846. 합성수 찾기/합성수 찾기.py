def solution(n):
    ans = 0
    for i in range(2, n+1):
        for k in range(2, i//2 + 1):
            if i % k == 0:
                ans += 1
                break
    return ans