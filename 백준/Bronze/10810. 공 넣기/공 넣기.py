n, m = map(int, input().split())
baskets = [[0] for i in range(n+1)]

for i in range(m):
    x, y, num = map(int, input().split())
    for k in range(x, y+1):
        baskets[k].append(num)

for i in range(1, len(baskets)):
    print(baskets[i][-1], end=' ')