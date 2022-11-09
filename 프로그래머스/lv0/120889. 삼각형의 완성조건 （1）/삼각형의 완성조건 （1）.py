def solution(sides):
    maxnum = max(sides)
    sides.remove(maxnum)
    return 1 if maxnum < sum(sides) else 2