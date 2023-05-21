n = list(input())
n = sorted(n, reverse=True)

if sum(map(int, n)) % 3 == 0 and n[-1] == '0':
    print(int(''.join(n)))
else:
    print(-1)