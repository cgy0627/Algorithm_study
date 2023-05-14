a,b = map(int, input().split())
check = {}
for i in range(a):
    check[input()] = 1

names = []
for i in range(b):
    name = input()
    if name in check:
        names.append(name)

names.sort()
print(len(names))
for name in names:
    print(name)