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
c,d = map(int, input().split())

nom, denom = a*d + b*c, b*d
gcd = gcd([nom, denom])

print(nom//gcd, denom//gcd)