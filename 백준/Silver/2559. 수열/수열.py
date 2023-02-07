import sys

N, K = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

maxtemp = sum(temp[:K])
acc_temp = [maxtemp]
for i in range(K, N):
    acc_temp.append(acc_temp[-1] - temp[i-K] + temp[i])
    if acc_temp[-1] > maxtemp:
        maxtemp = acc_temp[-1]
print(maxtemp)