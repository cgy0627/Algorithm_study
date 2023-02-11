import sys

n = int(input())
lst = list(zip(range(n), map(int, input().split())))

lst_sort = sorted(lst, key=lambda x: (x[1],x[0]))
lst_ord = []
index = -1
prev = 0
for idx, num in lst_sort:
    if num != prev:
        index += 1
    lst_ord.append((index, idx, num))
    prev = num

for elem in sorted(lst_ord, key=lambda x: x[1]):
    print(elem[0], end = ' ')