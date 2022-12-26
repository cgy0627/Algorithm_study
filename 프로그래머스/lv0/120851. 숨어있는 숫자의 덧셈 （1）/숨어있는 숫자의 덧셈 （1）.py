def solution(my_string):
    total = 0
    for char in my_string:
        try:
            int(char)
        except:
            char = char
        else:
            total += int(char)
    return total