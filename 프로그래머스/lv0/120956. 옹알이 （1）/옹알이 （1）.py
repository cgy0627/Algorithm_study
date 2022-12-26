def solution(babbling):
    count = 0
    for bab in babbling:
        for s in ["aya", "ye", "woo", "ma"]:
            if bab == "":
                break
            bab = bab.replace(s, ' ')
        if bab.strip() == '':
            count += 1
        print(bab, count)
    return count