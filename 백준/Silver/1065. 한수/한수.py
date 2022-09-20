# 1065 한수

N = int(input())

count = 0
for num in range(1, N + 1):
    num = str(num)
    diff = set()
    for i in range(len(num)-1):
        diff.add(int(num[i+1]) - int(num[i]))
    if (len(diff) == 0) | (len(diff) == 1):
        count += 1

print(count)