import sys

n, m = map(int, sys.stdin.readline().split())

A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
for i in range(n):
    B.append(list(map(sum, zip(A[i], map(int, sys.stdin.readline().split())))))

for i in range(len(B)):
    print(' '.join(map(str, B[i])))