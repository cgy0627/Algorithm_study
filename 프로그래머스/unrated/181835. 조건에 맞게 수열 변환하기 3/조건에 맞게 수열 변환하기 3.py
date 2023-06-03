def solution(arr, k):
    return list(map(lambda x: x*k, arr)) if k % 2 == 1 else list(map(lambda x: x+k, arr))