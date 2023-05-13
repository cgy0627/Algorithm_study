months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days = {0:"MON", 1:"TUE", 2:"WED", 3:"THU", 4:"FRI", 5:"SAT", 6:"SUN"}
m, d = map(int, input().split())

total = sum(months[i] for i in range(1, m)) + d - 1

print(days[total%7])