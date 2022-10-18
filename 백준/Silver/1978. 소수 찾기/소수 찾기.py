import sys

N = int(sys.stdin.readline())

def find_prime(num):
    if num <= 1:
        return False

    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

count = 0
nums = list(map(int, sys.stdin.readline().strip().split()))
for num in nums:
    count += find_prime(num)
    
print(count)