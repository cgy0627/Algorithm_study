def solution(n):
    ans = 0
    for i in range(1, n+1):
        total = i
        if total == n:
            ans += 1
        for k in range(i+1, n+1):
            total += k
            if total == n:
                ans += 1
            elif total > n:
                break
    return ans