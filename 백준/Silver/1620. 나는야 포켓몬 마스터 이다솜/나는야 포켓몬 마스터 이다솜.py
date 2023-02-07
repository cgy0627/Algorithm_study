import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = {}
poke_index = {}
for i in range(N):
    poke = sys.stdin.readline().strip()
    pokemon[i+1] = poke
    poke_index[poke] = i+1

for i in range(M):
    q = sys.stdin.readline().strip()
    try:
        q = int(q)
    except:
        print(poke_index[q])
        continue
    
    print(pokemon[q])