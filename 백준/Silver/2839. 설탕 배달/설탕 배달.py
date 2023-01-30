n = int(input())

ans = 0
while n >= 3:
    if n % 5 == 0:
        ans += (n // 5)
        n %= 5
    elif n >= 3:
        n -= 3
        ans += 1

print(ans if n == 0 else -1)