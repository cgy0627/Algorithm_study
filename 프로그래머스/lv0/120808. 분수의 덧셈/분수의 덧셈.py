def solution(numer1, denom1, numer2, denom2):
    n, d = numer1*denom2 + numer2*denom1, denom1*denom2
    
    i = 2
    while i <= min(n,d):
        if (n % i == 0) & (d % i == 0):
            n, d = n//i, d//i
            i = 2
        else:
            i += 1
    
    return [n,d]