N, C = map(int, input().split())
lst = list(map(int, input().split()))
lst_sort = list(map(str, sorted(lst, key=lambda x: (lst.count(x), -lst.index(x)), reverse=True)))

print(' '.join(lst_sort))