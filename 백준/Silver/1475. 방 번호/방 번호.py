n = input()
nums = [0] * 10

for char in n:
    if (char == "6") | (char == "9"):
        nums[9] += 1
    else:
        nums[int(char)] += 1

nums[9] = (nums[9]+1)//2
print(max(nums))