def solution(n, numlist):
    return list(filter(lambda x: x % n == 0, numlist))