import sys
import heapq

gift = []
for i in range(int(sys.stdin.readline())):
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] == 0:
        if gift:
            print(-heapq.heappop(gift))
        else:
            print(-1)
    else:
        for k in range(1, nums[0]+1):
            heapq.heappush(gift, -nums[k])