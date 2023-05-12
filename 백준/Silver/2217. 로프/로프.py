ropes = []
for i in range(int(input())):
    ropes.append(int(input()))

ropes = sorted(ropes, reverse=True)
weights = []
for i, rope in enumerate(ropes):
    weights.append(rope*(i+1))

print(max(weights))