def solution(n):
    res = ''
    for i in sorted(str(n), reverse = True):
        res += i
    return int(res)