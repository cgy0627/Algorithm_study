equation = input().split('-')

minus = []
for part in equation:
    if '+' in part:
        part = sum(map(int, part.split('+')))
    minus.append(int(part))

total = minus[0]
for i in range(1, len(minus)):
    total -= minus[i]

print(total)