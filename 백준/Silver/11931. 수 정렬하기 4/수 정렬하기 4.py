import sys
import heapq

n = int(input())

lst = [-int(sys.stdin.readline().strip()) for i in range(n)]

heapq.heapify(lst)
for i in range(n):
    print(-heapq.heappop(lst))