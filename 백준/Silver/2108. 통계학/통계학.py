import sys

N = int(sys.stdin.readline())

lst = []
dic = {}
for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

lst_sort = sorted(lst)

print(round(sum(lst_sort)/N))        # 산출평균
print(round(lst_sort[N//2]))         # 중앙값

comp = []
idx = 0
for k,v in sorted(dic.items(), key=lambda item: (-item[1], item[0])):
    idx += 1
    comp.append((k,v))
    if idx == 2:
        break

if len(comp) == 1:
    print(comp[0][0])
elif comp[0][1] != comp[1][1]:
    print(comp[0][0])
else:
    print(comp[1][0])

print(lst_sort[-1] - lst_sort[0])