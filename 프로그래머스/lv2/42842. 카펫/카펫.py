def solution(brown, yellow):
    w,h = (brown-6)//2+2, 3
    
    while True:
        if (w-2) * (h-2) == yellow:
            return [w,h]
        h += 1
        w = (brown-(h*2))//2 + 2