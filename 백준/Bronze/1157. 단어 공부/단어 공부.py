from collections import Counter

sample = input().lower()

char_cnt = Counter(sample)

sort_cnt = char_cnt.most_common()

if len(char_cnt) == 0:
    print('?')
elif len(char_cnt) == 1:
    print((char_cnt.most_common()[0][0]).upper())
elif sort_cnt[0][1] == sort_cnt[1][1]:
    print('?')
else:
    print((sort_cnt[0][0]).upper())