n = int(input())

i = 1
ans = 1
while i < n:
    i = i + 6*ans
    ans += 1

print(ans)