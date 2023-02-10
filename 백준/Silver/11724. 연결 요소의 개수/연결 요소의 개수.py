import sys
sys.setrecursionlimit(10**6)    # 파이썬 기본 재귀루프한도는 1000

N,M = map(int, sys.stdin.readline().split())

lst = [[] for i in range(N)]
check = [False] * N
ans = 0

for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    lst[u-1].append(v-1)
    lst[v-1].append(u-1)

def dfs(now):
    for link in lst[now]:
        if not check[link]:
            check[link] = True
            dfs(link)

for i in range(N):
    if not check[i]:
        ans += 1
        check[i] = True
        dfs(i)

print(ans)