from collections import deque

cards = deque(range(1, int(input())+1))

idx = 0
while len(cards) > 1:
    if idx % 2 == 0:
        print(cards.popleft(), end=" ")
    else:
        cards.rotate(-1)
    idx += 1

print(cards[0])