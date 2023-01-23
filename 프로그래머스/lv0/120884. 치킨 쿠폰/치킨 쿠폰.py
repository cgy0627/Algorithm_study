def solution(chicken):
    coupon = 0
    while chicken >= 10:
        new_coupon = chicken // 10
        coupon += new_coupon
        chicken = chicken % 10 + new_coupon
    return coupon