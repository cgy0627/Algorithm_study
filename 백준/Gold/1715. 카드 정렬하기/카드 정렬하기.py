import sys
import heapq

cards = []
for i in range(int(sys.stdin.readline())):
    heapq.heappush(cards, int(sys.stdin.readline()))

total = 0
while len(cards) > 1:
    comb = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, comb)
    total += comb

print(total)