n = int(input())
ans = 1
while n != 1:
    if n % 2 != 0:
        ans = 0
        break
    n /= 2
print(ans)