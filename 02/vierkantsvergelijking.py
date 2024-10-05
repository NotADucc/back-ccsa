import math 
a = float(input())
b = float(input())
c = float(input())

discri = b ** 2 - (4 * a * c)
if discri < 0 :
    print("geen wortels")    
elif discri == 0 :
    print("een wortel")
    print(b / (2 * a) * -1)
else :
    print("twee wortels")
    (x1, x2) = ((-b + math.sqrt(discri)) / (2 * a), (-b - math.sqrt(discri)) / (2 * a))
    if x1 < x2 :
        print(x1)
        print(x2)
    else :
        print(x2)
        print(x1)
    