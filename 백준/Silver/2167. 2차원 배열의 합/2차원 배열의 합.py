import sys

N, M = map(int, sys.stdin.readline().split())

acc_arr = [[0 for x in range(M+1)] for y in range(N+1)]

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        acc_arr[i+1][j+1] = acc_arr[i][j+1] + acc_arr[i+1][j] + lst[j] - acc_arr[i][j]

K = int(sys.stdin.readline())

for i in range(K):
    a,b,c,d = map(int, sys.stdin.readline().split())
    print(acc_arr[c][d] - acc_arr[a-1][d] - acc_arr[c][b-1] + acc_arr[a-1][b-1])