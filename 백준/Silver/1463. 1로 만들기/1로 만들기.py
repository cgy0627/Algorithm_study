n = int(input())

ans = [0] * (n+1)   # ans[i] = i가 1이 되기 위한 연산 횟수

for i in range(2, n+1):
    ans[i] = ans[i-1] + 1   # 디폴트로는 그 전 숫자에서 +1 한거니까 횟수도 그 전 숫자의 횟수에 +1 한것임
    if i % 3 == 0:
        ans[i] = min(ans[i], ans[i // 3] + 1)   # 디폴트와 x3 하기 전의 숫자의 횟수에서 +1 한거 중에 더 작은 수가 최적의 횟수!
    if i % 2 == 0:
        ans[i] = min(ans[i], ans[i // 2] + 1)   # 이미 들어있는 값과 x2 하기 전의 숫자의 횟수에서 +1 한거 중에 더 작은 수가 최적의 횟수!

print(ans[n])