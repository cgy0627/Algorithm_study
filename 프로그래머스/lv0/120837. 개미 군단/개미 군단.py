def solution(hp):
    count = 0
    while hp >= 5:
        hp -= 5
        count += 1
    while hp >= 3:
        hp -= 3
        count += 1
    while hp >= 1:
        hp -= 1
        count += 1
    
    return count