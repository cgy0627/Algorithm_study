ans = [0] * 12  # 문제에서 11까지만 input을 준다고 해서
ans[1], ans[2], ans[3] = 1, 2, 4

# 11까지의 숫자의 합 만드는 경우의 수 넣기기
for i in range(4, 12):
    ans[i] = sum(ans[i-3:i])

for i in range(int(input())):
    print(ans[int(input())])