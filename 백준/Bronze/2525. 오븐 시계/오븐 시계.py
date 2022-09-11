h, m = input().split()
oven_time = int(input())
h, m = int(h), int(m)

if m + oven_time < 60:
    m += oven_time
else:
    m += oven_time
    h_passed = m // 60
    m = m - h_passed * 60
    if h + h_passed >= 24:
        h = h + h_passed - 24
    else:
        h += h_passed

print(h, m)