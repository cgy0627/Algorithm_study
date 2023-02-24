n, m = map(int, input().split())
baskets = [i for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    baskets[x:y+1] = baskets[y:x-1:-1]

print(*baskets[1:])