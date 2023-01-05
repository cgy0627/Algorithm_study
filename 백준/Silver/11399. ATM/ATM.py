num = int(input())
mins = sorted([int(n) for n in input().split(' ')])

total = 0
for i in range(num):
    total += sum(mins[:i+1])

print(total)