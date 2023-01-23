def solution(sides):
    sides.sort()
    
    return len(range(sides[1] - sides[0] + 1, sides[1])) + len(range(sides[1], sum(sides)))