def solution(s):
    res = ''
    count = 0
    for char in s:
        if char == ' ':
            count = 0
            res += char
        else:
            count += 1
            if count % 2 == 0:
                res += char.lower()
            else:
                res += char.upper()
    
    return res

#     def updown(word):
#         return ''.join([word[i].upper() if i % 2 == 0 else word[i].lower() for i in range(len(word))])
    
#     return ' '.join(map(updown, s.split()))