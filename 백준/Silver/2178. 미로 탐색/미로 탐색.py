from collections import deque
import sys

M, N = map(int, sys.stdin.readline().strip().split())

def bfs(a, b):
    ans = []
    dq = deque()
    dq.append((1, a, b))
    while dq:
        idx, x, y = dq.popleft()
        if (x == M-1) & (y == N-1):
            ans.append(idx)
            continue
        
        if x+1 < M:
            if maze[x+1][y] == '1':
                dq.append((idx+1, x+1, y))
                maze[x+1][y] = '0'
        if y+1 < N:
            if maze[x][y+1] == '1':
                dq.append((idx+1, x, y+1))
                maze[x][y+1] = '0'
        if x-1 >= 0:
            if maze[x-1][y] == '1':
                dq.append((idx+1, x-1, y))
                maze[x-1][y] = '0'
        if y-1 >= 0:
            if maze[x][y-1] == '1':
                dq.append((idx+1, x, y-1))
                maze[x][y-1] = '0'
    return ans

maze = []
for i in range(M):
    maze.append(list(sys.stdin.readline().strip()))

print(min(bfs(0,0)))