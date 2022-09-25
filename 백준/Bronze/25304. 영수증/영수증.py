total = int(input())
num_items = int(input())

actual_total = 0
for i in range(num_items):
    info = list(map(int, input().split()))
    actual_total = actual_total + (info[0] * info[1])

if total == actual_total:
    print('Yes')
else:
    print('No')