def solution(order):
    ans = 0
    for char in str(order):
        if char in ['3', '6', '9']:
            ans += 1
    
    return ans