N, X = map(int, input().split())
A = list(map(int, input().split()))

res = ''
for num in A:
    if num < X:
        print(num, end = " ")