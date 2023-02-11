import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(N, M+1):
    if is_prime(num):
        primes.append(num)

if primes == []:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])