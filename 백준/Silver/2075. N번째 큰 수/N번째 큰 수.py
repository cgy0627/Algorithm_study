import heapq

N = int(input())
heap = []
for i in range(N):
    for num in map(int, input().split()):
        heapq.heappush(heap, num)
        if len(heap) > N:
            heapq.heappop(heap)

print(heapq.heappop(heap))