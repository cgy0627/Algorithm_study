def solution(arr, idx):
    ans = idx
    while sum(arr[ans:]) > 0:
        if arr[ans]:
            return ans
        ans += 1
    
    return -1