import sys

checklist = set(range(1, 31))
for i in range(28):
    checklist -= {int(sys.stdin.readline())}

for num in sorted(list(checklist)):
    print(num)