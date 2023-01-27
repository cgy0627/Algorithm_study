import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        print((heapq.heappop(heap))*(-1) if heap != [] else 0)
    else:
        heapq.heappush(heap, -num)