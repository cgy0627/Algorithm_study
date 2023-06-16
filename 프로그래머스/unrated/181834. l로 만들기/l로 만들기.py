def solution(myString):
    ans = ''
    for char in myString:
        if ord(char) < ord('l'):
            ans += 'l'
        else:
            ans += char
    
    return ans