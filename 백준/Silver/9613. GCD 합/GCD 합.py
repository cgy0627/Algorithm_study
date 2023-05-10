from itertools import combinations

def gcd(pair):
    a,b = min(pair), max(pair)

    if a == 0 or b == 1:
        return b
    
    if b % a == 0:
        return a
    
    while b % a != 0:
        a,b = b%a, a
    return a

for i in range(int(input())):
    nums = list(map(int, input().split()))
    combs = list(combinations(nums[1:], 2))
    print(sum(map(gcd, combs)))