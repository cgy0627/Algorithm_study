n = int(input())
for i in range(n):
    line = list(input().split(' '))
    print(' '.join(map(lambda x: x[::-1], line)))