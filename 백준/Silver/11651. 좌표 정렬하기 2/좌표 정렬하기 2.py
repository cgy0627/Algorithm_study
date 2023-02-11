import sys

lst = []
for i in range(int(sys.stdin.readline())):
    lst.append(list(map(int, sys.stdin.readline().split())))

for a,b in sorted(lst, key=lambda x: (x[1], x[0])):
    print(a, b)