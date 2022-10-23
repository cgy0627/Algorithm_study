def solution(s):
    a = str(min(map(int, s.split())))
    b = str(max(map(int, s.split())))
    return a + ' ' + b