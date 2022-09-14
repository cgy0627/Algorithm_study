def solution(n, arr1, arr2):
    res = []
    for i in range(len(arr1)):
        num1 = int(str(bin(arr1[i]))[2:])
        num2 = int(str(bin(arr2[i]))[2:])
        comb = str(num1 + num2)
        
        if len(comb) < n:
            comb = '0'*(n-len(comb)) + comb
        
        res.append(''.join(['#' if int(i) > 0 else ' ' for i in comb]))
        
    return res