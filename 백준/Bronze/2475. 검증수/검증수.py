import sys

nums = list(map(int, sys.stdin.readline().split()))
total = 0
for num in nums:
    total += num * num

print(total % 10)