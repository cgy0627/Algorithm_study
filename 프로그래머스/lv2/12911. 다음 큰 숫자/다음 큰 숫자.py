def solution(n):
    ones = bin(n)[2:].count('1')
    
    while True:
        n += 1
        if ones == bin(n)[2:].count('1'):
            return n