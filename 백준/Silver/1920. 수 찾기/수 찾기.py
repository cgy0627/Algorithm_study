import sys

a = int(sys.stdin.readline())
N = sys.stdin.readline().split()
N_dict = dict(zip(N, [1] * len(N)))

b = int(sys.stdin.readline())
M = sys.stdin.readline().split()

for num in M:
    print(int(num in N_dict))