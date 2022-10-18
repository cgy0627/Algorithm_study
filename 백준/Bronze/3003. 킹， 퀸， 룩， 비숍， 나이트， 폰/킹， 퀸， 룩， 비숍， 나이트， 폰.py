import sys

pieces = list(map(int, sys.stdin.readline().split()))
original = [1,1,2,2,2,8]

for i in range(len(original)):
    original[i] -= pieces[i]

print(' '.join(map(str, original)))