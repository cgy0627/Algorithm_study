nums = list(map(int, input().split()))

prev = nums[1] - nums[0]
for i in range(2, len(nums)):
    if prev != nums[i] - nums[i-1]:
        prev = 0
        break

if prev > 0:
    print("ascending")
elif prev < 0:
    print("descending")
else:
    print("mixed")