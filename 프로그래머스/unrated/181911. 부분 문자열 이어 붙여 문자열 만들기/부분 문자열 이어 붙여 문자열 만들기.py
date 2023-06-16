def solution(my_strings, parts):
    return ''.join([my_strings[i][x[0]:x[1]+1] for i, x in enumerate(parts)])