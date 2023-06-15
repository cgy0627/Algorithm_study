def solution(arr, n):
    return [arr[i] + n if int(len(arr) % 2 != i % 2) else arr[i] for i in range(len(arr))]