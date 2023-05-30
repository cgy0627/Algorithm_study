n = int(input())
for i in range(1, n*2, 2):
    padding = (2*n-1)//2 + 1 + i//2
    res = '*' * i
    print(f'{res:>{padding}}')