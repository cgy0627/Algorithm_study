def solution(str_list, ex):
    ans = ''
    for word in str_list:
        if ex not in word:
            ans += word
    return ans