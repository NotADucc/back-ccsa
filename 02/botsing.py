r1x1 = int(input())
r1y1 = int(input())
r1x2 = int(input())
r1y2 = int(input())
(r1x1, r1x2) = (r1x1, r1x2) if r1x1 < r1x2 else (r1x2, r1x1)
(r1y1, r1y2) = (r1y1, r1y2) if r1y1 < r1y2 else (r1y2, r1y1)
r2x1 = int(input())
r2y1 = int(input())
r2x2 = int(input())
r2y2 = int(input())
(r2x1, r2x2) = (r2x1, r2x2) if r2x1 < r2x2 else (r2x2, r2x1)
(r2y1, r2y2) = (r2y1, r2y2) if r2y1 < r2y2 else (r2y2, r2y1)


if (r2x1 >= r1x1 and r2x1 < r1x2) or (r2x2 > r1x1 and r2x2 <= r1x2) :
    if (r2y1 >= r1y1 and r2y1 < r1y2) or (r2y2 > r1y1 and r2y2 <= r1y2):
        print("botsing")
    else :
        print("geen botsing")
else :
    print("geen botsing")