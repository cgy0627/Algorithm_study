ans = [0] * 1001
ans[1], ans[2] = 1, 2

for i in range(3, 1001):
    ans[i] = ans[i-1] + ans[i-2]

print(ans[int(input())] % 10007)