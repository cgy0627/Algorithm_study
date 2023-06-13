def solution(n, control):
    con = {'w':'1', 's':'(-1)', 'd':'10', 'a':'(-10)'}
    return n + eval('+'.join([con[char] for char in control]))