N = int(input())

words = set(input() for i in range(N))

for word in sorted(words, key=lambda x:(len(x), x)):
    print(word)