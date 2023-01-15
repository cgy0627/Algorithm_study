word = input()

croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for letter in croatian:
    word = word.replace(letter, "0")

print(len(word))