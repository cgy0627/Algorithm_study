import sys

lst = []
for i in range(int(sys.stdin.readline())):
    a,b = sys.stdin.readline().split()
    lst.append((int(a), b, i))

for a,b,c in sorted(lst, key=lambda x: (x[0], x[2])):
    print(a, b)