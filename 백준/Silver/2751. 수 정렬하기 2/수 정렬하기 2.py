import sys
import heapq

n = int(input())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

heapq.heapify(lst)
for i in range(n):
    print(heapq.heappop(lst))