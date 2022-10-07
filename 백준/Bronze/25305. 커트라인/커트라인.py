import sys

N, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))
scores.sort(reverse=True)

print(scores[k-1])