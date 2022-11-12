def solution(s1, s2):
    return len(set(s1) & set(s2))
    # return (len(s1) + len(s2)) - (len(set(s1).add(set(s2))))