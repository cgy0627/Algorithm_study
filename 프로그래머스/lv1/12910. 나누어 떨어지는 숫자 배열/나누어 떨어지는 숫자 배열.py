def solution(arr, divisor):
    res = [arr[i] for i in range(len(arr)) if arr[i] % divisor == 0]
    if res:
        return sorted(res)
    return [-1]