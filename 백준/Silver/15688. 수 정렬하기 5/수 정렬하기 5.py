import sys

n = int(input())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for num in lst:
    print(num)