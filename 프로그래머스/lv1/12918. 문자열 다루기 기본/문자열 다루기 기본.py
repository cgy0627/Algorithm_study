def solution(s):
    return ((len(s) == 6) | (len(s) == 4)) & s.isdigit()
        