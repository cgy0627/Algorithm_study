def solution(arr, intervals):
    ans = []
    for s,e in intervals:
        ans += arr[s:e+1]
    
    return ans