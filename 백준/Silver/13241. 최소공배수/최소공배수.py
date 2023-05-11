def gcd(pair):
    a,b = min(pair), max(pair)

    if a == 0 or b == 1:
        return b
    
    if b % a == 0:
        return a
    
    while b % a != 0:
        a,b = b%a, a
    return a
    
a,b = map(int, input().split())
ab_gcd = gcd([a,b])

print(a*b//ab_gcd)