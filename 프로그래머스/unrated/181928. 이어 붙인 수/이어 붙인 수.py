def solution(num_list):
    evens, odds = [], []
    for num in num_list:
        if num % 2 == 0:
            evens.append(str(num))
        else:
            odds.append(str(num))
    
    return int(''.join(evens)) + int(''.join(odds))