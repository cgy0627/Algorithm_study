import sys
nums = sys.stdin.readline().strip()
while nums:
    a, b = map(int, nums.split())
    print(a + b)
    nums = sys.stdin.readline().strip()