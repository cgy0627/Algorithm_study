# 4673 셀프 넘버

res = [i for i in range(10001)]

for i in range(10001):
    num = sum([i] + [int(n) for n in str(i)])
    #print([i] + [int(n) for n in str(i)], num)
    
    if num in res:
        res.remove(num)

for n in res:
    print(n)