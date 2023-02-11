lst = []
for i in range(5):
    lst.append(int(input()))

lst_sort = sorted(lst)
print(int(sum(lst_sort)/5))
print(lst_sort[2])