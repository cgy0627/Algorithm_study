def solution(a, b):
    b_div = []
    
    num = 2
    while num <= b//2:
        if b % num == 0:
            if num not in [2,5]:
                b_div.append(num)
            b = b//num
        else:
            num += 1
    if b not in [2,5]:
        b_div.append(b)
    
    num = 2
    while num <= a//2:
        if a % num == 0:
            try:
                b_div.remove(num)
            except:
                pass
            a = a//num
        else:
            num += 1
    try:
        b_div.remove(a)
    except:
        pass
    
    print(b_div)
    return 1 if b_div == [] else 2