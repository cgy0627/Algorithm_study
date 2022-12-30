def solution(my_string):
    ans = []
    for char in my_string:
        if char.isnumeric():
            ans.append(int(char))
    return sorted(ans)