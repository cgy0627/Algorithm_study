word = input()
while len(word) >= 10:
    print(word[:10])
    word = word[10:]

if len(word) > 0:
    print(word)