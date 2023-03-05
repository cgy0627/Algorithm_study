alphabet = [0 for i in range(26)]
for char in input():
    alphabet[ord(char) - 97] += 1

print(' '.join(map(str, alphabet)))