def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X += [arr[i]] * arr[i] * 2
        else:
            X = X[:-1*arr[i]]
        
    return X