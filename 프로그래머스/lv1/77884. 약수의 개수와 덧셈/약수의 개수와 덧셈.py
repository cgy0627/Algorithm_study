def solution(left, right):
    nums = []
    for num in range(left, right+1):
        if int(num**0.5 + 0.5) ** 2 == num:
            nums.append(-num)
        else:
            nums.append(num)
    return sum(nums)
        