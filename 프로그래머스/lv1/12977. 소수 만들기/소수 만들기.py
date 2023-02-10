def solution(nums):
    from itertools import combinations
    
    combs = map(sum, combinations(nums, 3))
    
    ans = 0
    for num in combs:
        ans += 1
        for i in range(2, num//2):
            if num % i == 0:    # 나눠지면 소수가 아님
                ans -= 1
                break
    
    return ans