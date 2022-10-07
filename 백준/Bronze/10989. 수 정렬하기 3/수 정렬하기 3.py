import sys

n = int(input())

lst = [0]*10001
for i in range(n):
    lst[int(sys.stdin.readline().strip())] += 1

for i in range(len(lst)):
    if lst[i] == 0:
        next
    for j in range(lst[i]):
        print(i)