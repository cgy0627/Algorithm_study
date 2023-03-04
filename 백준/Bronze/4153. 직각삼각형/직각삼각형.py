import heapq

while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    heap = [a,b,c]
    heapq.heapify(heap)
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = heapq.heappop(heap)

    if (a/2)**2 + (b/2)**2 == (c/2)**2:
        print("right")
    else:
        print("wrong")