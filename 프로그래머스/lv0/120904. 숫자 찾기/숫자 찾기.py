def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k)) + 1
    else:
        return -1