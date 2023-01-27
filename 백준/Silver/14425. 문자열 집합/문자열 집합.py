n,m = map(int, input().split())

S = []
for i in range(n):
    S.append(input())

ans = 0
for i in range(m):
    if input() in S:
        ans += 1

print(ans)