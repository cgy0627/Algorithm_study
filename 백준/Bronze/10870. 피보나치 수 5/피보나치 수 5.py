# 0 1 1 2 3 5 8 13 21 34
N = int(input())
a,b = 0,1
idx = N
while(idx >= 2):
    a,b = b, a+b
    idx -= 1

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    print(b)