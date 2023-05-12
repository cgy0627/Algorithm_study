change = 1000 - int(input())

en = [500, 100, 50, 10, 5, 1]
count = 0
for coin in en:
    if coin > change:
        continue
    
    count += change // coin
    change %= coin

    if change == 0:
        break

print(count)