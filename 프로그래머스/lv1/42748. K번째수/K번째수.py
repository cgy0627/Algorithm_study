def solution(array, commands):
    res = []
    for i, j, k in commands:
        #print(sorted(array[i-1:j])[k-1])
        res.append(sorted(array[i-1:j])[k-1])
        
    return res