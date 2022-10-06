N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

for num in sorted(lst):
    print(num)