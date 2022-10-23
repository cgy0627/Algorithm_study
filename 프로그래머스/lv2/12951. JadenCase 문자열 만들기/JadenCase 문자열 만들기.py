def solution(s):
    new_word = True
    res = ''
    for char in s.lower():
        if char == ' ':
            new_word = True
        elif new_word:
            char = char.upper()
            new_word = False
            
        res += char
    
    return res