words = []
for i in range(5):
    word = input()
    words.append(list(word + ' ' * (15 - len(word))))

print(''.join([''.join(lst) for lst in zip(words[0], words[1], words[2], words[3], words[4])]).replace(' ', ''))