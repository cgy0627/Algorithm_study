def solution(array):
    lst = list(set([(x, array.count(x)) for x in array]))
    lst_sort = sorted(lst, key=lambda x: x[1], reverse=True)
    
    if len(lst_sort) == 1:
        return lst_sort[0][0]
    else:
        return lst_sort[0][0] if lst_sort[0][1] != lst_sort[1][1] else -1