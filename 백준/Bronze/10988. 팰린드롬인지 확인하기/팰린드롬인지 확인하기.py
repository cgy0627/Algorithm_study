word = input()
wordlen = len(word)

if wordlen % 2 == 0:
    print(1 if word[:wordlen//2] == word[wordlen//2:][::-1] else 0)
else:
    print(1 if word[:wordlen//2] == word[wordlen//2+1:][::-1] else 0)