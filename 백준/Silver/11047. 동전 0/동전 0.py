num, total = input().split()
# num, total = 10, 4200

total = int(total)
coins = []
for i in range(int(num)):
    coins.append(int(input()))
        
count = 0
for i in range(len(coins)-1, -1, -1):
    if total == 0:
        break
    if coins[i] <= total:
        times = total // coins[i]
        total %= coins[i]
        count += times

print(count)