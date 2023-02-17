ans = 0
check = False
for i in range(5):
    n = int(input())
    if n < 40:
        ans += 40
    else:
        ans += n

print(ans//5)