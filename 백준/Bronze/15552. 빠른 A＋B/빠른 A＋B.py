import sys

n = int(input().strip())

while n > 0:
    a,b = map(int, sys.stdin.readline().strip().split())
    print(a + b)
    n -= 1