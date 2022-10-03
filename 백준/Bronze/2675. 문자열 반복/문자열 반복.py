num_samples = int(input())

for num in range(num_samples):
    repeat, word = input().split()
    new_word = ''.join([char * int(repeat) for char in word])
    print(new_word)