h,m = input().split()
h,m = int(h), int(m)

if m >= 45:
    m -= 45
else:
    m = m - 45 + 60
    if h == 0:
        h = h -1 + 24
    else:
        h -= 1

print(h, m)