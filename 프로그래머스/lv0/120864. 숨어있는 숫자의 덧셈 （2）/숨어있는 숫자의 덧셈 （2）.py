def solution(my_string):
    nums = list(map(str, range(0,10)))
    for char in my_string:
        if char not in nums:
            my_string = my_string.replace(char, " ")
    
    ans = my_string.split()
    
    if ans == []:
        return 0
    return sum(map(int, ans))