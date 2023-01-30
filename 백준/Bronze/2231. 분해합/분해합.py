import sys

N = int(input())

def bunhae(N):
    start = 0
    if N > 20:
        start = N-(len(str(N))*9)
    for i in range(start, N):
        nums = list(map(int, str(i)))
        if i + sum(nums) == N:
            return i
    return 0

print(bunhae(N))
