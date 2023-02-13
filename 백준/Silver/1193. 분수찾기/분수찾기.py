n = int(input())

x,y = 1,1
idx = 2
while n != 1:
    n -= 1
    increase = 0
    if idx % 2 == 0:
        y += 1
        if n == 1:
            break
        increase = idx-1 if n > idx-1 else n-1
        x, y = x + increase, y - increase
    else:
        x += 1
        if n == 1:
            break
        increase = idx-1 if n > idx-1 else n-1
        x, y = x - increase, y + increase

    n -= increase
    idx += 1

print(f'{x}/{y}')