def solution(a, d, included):
    return sum([num * included[i] for i, num in enumerate(range(a, a + d * len(included), d))])