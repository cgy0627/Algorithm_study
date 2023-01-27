n, k = map(int, input().split())

lst = list(range(1, n+1))
print("<", end="")
idx = k - 1
for i in range(n-1):
    print(lst.pop(idx), end=", ")
    idx = (idx + (k-1)) % len(lst)
print(lst[0], ">", sep="")