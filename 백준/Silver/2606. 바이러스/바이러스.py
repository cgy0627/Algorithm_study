import sys

N = int(sys.stdin.readline())

network = [[] for i in range(N+1)]
infected = [False] * (N+1)

def dfs(virus):
    infected[virus] = True
    for comp in network[virus]:
        if not infected[comp]:
            dfs(comp)

for i in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

dfs(1)

print(sum(infected)-1)