import heapq
import sys

heap = []
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(n), n))