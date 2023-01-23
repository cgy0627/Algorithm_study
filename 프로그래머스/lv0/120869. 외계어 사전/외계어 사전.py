def solution(spell, dic):
    import re
    ans = [1] * len(spell)
    
    for word in dic:
        if list(map(lambda x: word.count(x), spell)) == ans:
            return 1
    return 2
        