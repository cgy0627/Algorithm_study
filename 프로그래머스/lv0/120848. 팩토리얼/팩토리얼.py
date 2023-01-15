def solution(n):
    ans = 0
    product = 1
    while True:
        ans += 1
        product *= ans
        
        if product * (ans+1) > n:
            break
            
    return ans