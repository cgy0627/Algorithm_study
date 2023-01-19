def solution(my_string):
    addition = my_string.split(" + ")
    ans = 0
    for phrase in addition:
        if "-" in phrase:
            subtraction = phrase.split(" - ")
            a = int(subtraction[0])
            for i in range(1, len(subtraction)):
                a -= int(subtraction[i])
            ans += a
        else:
            ans += int(phrase)
    return ans
                