import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
M = int(input())
acc_lst = [0]

for i in range(N):
    acc_lst.append(acc_lst[i]+lst[i])

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    print(acc_lst[b] - acc_lst[a-1])