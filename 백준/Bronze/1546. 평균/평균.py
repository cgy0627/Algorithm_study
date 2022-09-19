# 1546 평균

N = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)

total = 0
for score in scores:
    total += (score/maxScore * 100)

print(total/len(scores))