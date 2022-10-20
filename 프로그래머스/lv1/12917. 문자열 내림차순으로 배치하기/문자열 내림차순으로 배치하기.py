def solution(s):
    chars = [char for char in s]
    return ''.join(sorted(chars, key=lambda x: ord(x), reverse = True))