import sys

a = int(sys.stdin.readline())
N = sys.stdin.readline().split()
N_dict = dict(zip(N, [1] * len(N)))
b = int(sys.stdin.readline())
M = sys.stdin.readline().split()
print(' '.join(list(map(lambda x: str(int(x in N_dict)), M))))