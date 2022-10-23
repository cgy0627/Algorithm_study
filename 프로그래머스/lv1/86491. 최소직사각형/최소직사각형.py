def solution(sizes):
    width = [max(a,b) for (a,b) in sizes]
    height = [min(a,b) for (a,b) in sizes]
    
    return max(width) * max(height)