def solution(s, n):
    res = ''
    for char in s:
        if char != " ":
            if 65 <= ord(char) <= 90:   # Uppercase
                res += chr((ord(char) + n - 65) % 26 + 65)
            else:
                res += chr((ord(char) + n - 97) % 26 + 97)
        else:
            res += char
    
    return res