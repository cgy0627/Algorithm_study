import sys

N = int(input())

meetings = [list(map(int, input().split())) for i in range(N)]
# meetings = [list(map(int, sys.stdin.readlin().split())) for i in range(N)]

meetings.sort(key=lambda x: (x[0],x[1]))

res = []
for meeting in meetings:
    start, end = meeting
    duration = end - start
    if res == []:
        res.append(meeting)
    else:
        if res[-1][1] > end:
            res.pop()
            res.append(meeting)
        elif res[-1][1] <= start:
            res.append(meeting)
print(len(res))