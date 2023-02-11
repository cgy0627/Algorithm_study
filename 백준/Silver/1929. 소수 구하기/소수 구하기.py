import sys

M, N = map(int, sys.stdin.readline().split())

primes = [True] * (N+1)
primes[1] = False

for i in range(2, N+1):
    for k in range(2, N+1):
        if i*k > N:
            break
        primes[i*k] = False

for num in range(M, N+1):
    if primes[num]:
        print(num)