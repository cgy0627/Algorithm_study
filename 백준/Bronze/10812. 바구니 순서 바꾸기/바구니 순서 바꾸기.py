n, m = map(int, input().split())
baskets = [i for i in range(n+1)]

for i in range(m):
    x, y, point = map(int, input().split())
    baskets[x:y+1] = baskets[point:y+1] + baskets[x:point]

print(*baskets[1:])