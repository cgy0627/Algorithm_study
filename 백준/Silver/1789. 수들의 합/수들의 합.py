n = int(input())

count = 0
for i in range(1, 4294967296):
    n -= i
    count += 1

    if n <= i:
        break

print(count)