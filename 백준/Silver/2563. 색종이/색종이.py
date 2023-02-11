paper = [[0] * 100 for i in range(100)]
for i in range(int(input())):
    a,b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            paper[x][y] += 1

print(10000 - sum(map(lambda x: x.count(0), paper)))