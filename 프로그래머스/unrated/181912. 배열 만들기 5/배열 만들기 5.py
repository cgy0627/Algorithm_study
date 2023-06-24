def solution(intStrs, k, s, l):
    return [int(x[s:s+l]) for x in intStrs if int(x[s:s+l]) > k]