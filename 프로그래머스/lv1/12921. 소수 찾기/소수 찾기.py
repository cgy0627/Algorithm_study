def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)

#     primes = [2]
#     for i in range(3, n+1, 2):
#         is_prime = True
#         for prime in primes:
#             if prime > i ** 0.5:
#                 break
#             elif i % prime == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             primes.append(i)
    
#     return len(primes)