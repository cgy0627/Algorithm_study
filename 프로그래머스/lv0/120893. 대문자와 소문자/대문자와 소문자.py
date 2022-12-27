def solution(my_string):
    ans = ""
    for char in my_string:
        if char.isupper():
            ans += char.lower()
        else:
            ans += char.upper()
    return ans