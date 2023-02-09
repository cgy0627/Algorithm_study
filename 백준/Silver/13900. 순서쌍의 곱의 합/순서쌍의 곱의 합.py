import sys

N = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
ans = 0
for i in range(0, N-1):
    total -= nums[i]
    ans += total * nums[i]

print(ans)