# 4344 평균은 넘겠지

N = int(input())
for i in range(N):
    scores = list(map(int, input().strip().split()))
    avg = sum(scores)/scores[0]
    print(f'{(len([score for score in scores[1:] if score >= int(avg)])/scores[0]*100 ):.3f}%')