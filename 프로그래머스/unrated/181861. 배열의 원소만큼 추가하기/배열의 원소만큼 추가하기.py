def solution(arr):
    X = []
    for num in arr:
        X += [num] * num
    return X