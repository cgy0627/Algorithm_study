from collections import deque
import sys

N,M,V = map(int, sys.stdin.readline().split())

lst = [[0] * N for i in range(N)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    lst[a-1][b-1] = 1
    lst[b-1][a-1] = 1

check = [False] * N
dfs_ans = [str(V)]
def dfs(now):
    check[now] = True
    for i in range(N):
        if (lst[now][i]) & (not check[i]):
            check[i] = True
            dfs_ans.append(str(i+1))
            dfs(i)

def bfs(now):
    ans = [str(now+1)]
    dq = deque()
    dq.append(now)
    while dq:
        num = dq.popleft()
        for i in range(N):
            if (lst[num][i]) & (str(i+1) not in ans):
                dq.append(i)
                ans.append(str(i+1))
    return ans

dfs(V-1)
print(' '.join(dfs_ans))
print(' '.join(bfs(V-1)))