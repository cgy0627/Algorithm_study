n, m = map(int, input().split())
baskets = [i for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    baskets[x], baskets[y] = baskets[y], baskets[x]

for i in range(1, len(baskets)):
    print(baskets[i], end=' ')