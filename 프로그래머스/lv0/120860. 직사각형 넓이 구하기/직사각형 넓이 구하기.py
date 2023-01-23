def solution(dots):
    x, y = set(), set()
    for nums in dots:
        x.add(nums[0])
        y.add(nums[1])
    
    return diff(x.pop(), x.pop()) * diff(y.pop(), y.pop())

def diff(a, b):
    return abs(a-b)