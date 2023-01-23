def solution(s):
    import re
    
    s = re.sub("-?\d+ Z ?", "", s)
    
    return sum(map(int, s.split()))