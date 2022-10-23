def solution(s):
    nums = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    
    ints = list(map(str, range(0,10)))
    res = ''
    word = ''
    for char in s:
        if char in ints:
            res += char
        else:
            word += char
            if word in nums:
                res += nums[word]
                word = ''
    
    return int(res)