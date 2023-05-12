n = int(input())
towers = list(map(int, input().split()))

count = 1
prev = towers[0]
for i in range(1, len(towers)):
    if towers[i] >= prev:
        count += 1
    prev = towers[i]

print(count)