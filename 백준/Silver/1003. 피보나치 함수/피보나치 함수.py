zero = [1] * 41     # fibonacci(0)이 호출되는 횟수
one = [1] * 41      # fibonacci(1)이 호출되는 횟수

zero[1]  = 0
one[0]= 0

# 0과 1이 호출되는 각각의 횟수 구하기
for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

for i in range(int(input())):
    n = int(input())
    print(zero[n], one[n])