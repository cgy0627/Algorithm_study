import sys
from itertools import combinations

N, M = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

sums = list(sorted(map(sum, combinations(cards, 3))))
ans = 0
for num in sums:
    if num == M:
        ans = num
        break
    if num > M:
        break
    ans = num

print(ans)