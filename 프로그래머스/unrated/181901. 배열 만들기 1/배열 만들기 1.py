def solution(n, k):
    i = 1
    ans = []
    while i * k <= n:
        ans.append(i * k)
        i += 1
    return ans