def solution(arr):
    return [x // 2 if x >= 50 and x % 2 == 0 else x * 2 if x < 50 and x % 2 == 1 else x for x in arr]