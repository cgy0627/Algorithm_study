def solution(my_string):
    import re
    return re.sub('[aeiou]', '', my_string)