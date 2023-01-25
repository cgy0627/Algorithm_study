def solution(n):
    ans = 0
    for i in range(1, n+1):
        ans += 1
        while (ans % 3 == 0) | (list(str(ans)).count('3') > 0):
            ans += 1
    return ans