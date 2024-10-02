import math
num = float(input())

prijs1 = 0
prijs2 = 0
prijs3 = num
i = 1

while (not math.isclose(prijs1 * prijs2 * prijs3, num)) :
    prijs1 = i / 100
    prijs2 = 0.01
    prijs3 = num - (prijs1 + prijs2)
    while (prijs2 < prijs3 and not math.isclose(prijs1 * prijs2 * prijs3, num)) :
        if prijs1 * prijs2 * prijs3 > num :
            break
        prijs2 += 0.01
        prijs3 = num - (prijs1 + prijs2)
    i += 1
 

prijs1 = format(prijs1, ".2f")
prijs2 = format(prijs2, ".2f")
prijs3 = format(prijs3, ".2f")
num = format(num, ".2f")
print(f'€{prijs1} + €{prijs2} + €{prijs3} = €{prijs1} x €{prijs2} x €{prijs3} = €{num}')