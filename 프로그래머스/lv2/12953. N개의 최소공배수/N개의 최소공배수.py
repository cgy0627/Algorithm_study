def solution(arr):
    import math
    
    ans = abs(arr[0] * arr[1]) // math.gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        ans = abs(ans * arr[i]) // math.gcd(ans, arr[i])
    
    return ans