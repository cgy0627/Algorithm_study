def solution(people, limit):
    people.sort(reverse=True)
    ans = 0
    light, heavy = len(people)-1, 0
    while heavy <= light:
        ans += 1
        if limit - people[heavy] >= people[light]:
            light -= 1
        heavy += 1
        
    return ans

    # people.sort()
    # ans = 0
    # while people != []:
    #     ans += 1
    #     for i in range(len(people)-1, 0, -1):
    #         if (limit - people[0]) - people[i] >= 0:    # 같이 탈 수 있는 젤 무거운 사람 찾기
    #             people.pop(i)
    #             break
    #         else:   # 한번 짝을 못 찾은 엄청 무거운 사람들은 어차피 혼자 타야함
    #             people.pop(i)
    #             ans += 1
    #     people.pop(0)
    # return ans