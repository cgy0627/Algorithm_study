# 10818 최소, 최대
import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().strip().split(' ')))

print(min(nums), max(nums))