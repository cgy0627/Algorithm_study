from collections import Counter

dice = list(map(int, input().split()))

dice_counter = Counter(dice)

for key,value in sorted(dice_counter.items(), key=lambda item: item[1], reverse = True):
    if value == 3:
        print(10000 + key * 1000)
        break
    elif value == 2:
        print(1000 + key * 100)
        break
    else:
        print(max(dice) * 100)
        break