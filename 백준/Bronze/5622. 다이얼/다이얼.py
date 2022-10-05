sample = input()
numbers = ['abc', 3, 'def', 4, 'ghi', 5, 'jkl', 6, 'mno', 7, 'pqrs', 8, 'tuv', 9, 'wxyz', 10]
num_dict = {}

for i in range(0, len(numbers), 2):
    for j in range(len(numbers[i])):
        num_dict[numbers[i][j]] = numbers[i+1]

ans = 0
for char in sample:
    ans += num_dict[char.lower()]

print(ans)