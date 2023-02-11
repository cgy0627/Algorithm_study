maxn = -1
x,y = 0,0
for i in range(1,10):
    row = zip(range(1,10), map(int, input().split()))
    row_sort = sorted(row, key=lambda x: (-x[1], -x[0]))
    if maxn <= row_sort[0][1]:
        maxn = row_sort[0][1]
        x,y = i,row_sort[0][0]
    
print(maxn)
print(x, y)