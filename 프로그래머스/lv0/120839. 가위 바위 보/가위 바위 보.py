def solution(rsp):
    ans = ""
    for hand in rsp:
        if hand == "0":
            ans += "5"
        elif hand == "2":
            ans += "0"
        else:
            ans += "2"
    return ans