start = 0
count = 0
for i in range(8):
    line = input()
    count += sum(line[j] == 'F' for j in range(start, 8, 2))
    start = 1 if not start else 0

print(count)