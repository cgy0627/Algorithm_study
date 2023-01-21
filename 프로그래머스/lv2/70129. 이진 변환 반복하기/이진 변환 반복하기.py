def solution(s):
    rounds = 0
    zero_removed = 0
    
    while s != '1':
        rounds += 1
        zero_removed += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]
    
    return [rounds, zero_removed]