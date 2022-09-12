import math
def solution(n):
    rooted = math.sqrt(n)
    if rooted - int(rooted) == 0:
        return (math.sqrt(n) + 1) ** 2
    return -1