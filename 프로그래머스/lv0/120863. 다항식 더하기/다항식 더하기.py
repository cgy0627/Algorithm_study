def solution(polynomial):
    if polynomial == "":
        return ""
    lst = polynomial.split(" + ")
    
    xnum, rnum = 0, 0
    for elem in lst:
        if 'x' in elem:
            if elem[0] == 'x':
                xnum += 1
            else:
                xnum += int(elem[:-1])
        else:
            rnum += int(elem)
    
    if xnum == 0:
        if rnum == 0:
            return ""
        else:
            return f'{rnum}'
    if xnum == 1:
        if rnum == 0:
            return f'x'
        else:
            return f'x + {rnum}'
    else:
        if rnum == 0:
            return f'{xnum}x'
        else:
            return f'{xnum}x + {rnum}'