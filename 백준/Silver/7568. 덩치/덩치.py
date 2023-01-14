n = int(input())

data = [list(map(int, input().split()))]
comp = [0] * n
for i in range(1, n):
    x, y = map(int, input().split())

    for k, (a, b) in enumerate(data):
        if (x > a) & (y > b):
            comp[k] += 1
        elif (x < a) & (y < b):
            comp[i] += 1
        
    data.append([x, y])

for num in comp:
    print(num+1, end=' ')