def solution(age):
    import string
    
    ans = ""
    
    alphabets = list(string.ascii_lowercase)
    ages = dict(zip(map(str, range(0,len(alphabets))), alphabets))
    
    for char in str(age):
        ans += ages[char]
    
    return ans