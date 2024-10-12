# # een beetje uitleg op wat er moet gebeuren zou fijn zijn.
# # nu een deel van probleemoplossend denken in algoritmes is kan er pre computed worden.
# # in dit geval wel waardoor er tijd bespaard wordt door duur rekenwerk over te slaan.

# print(1.63498390018)
# print(100)
from math import pi
def help(total) :
    s = 0
    for i in range(1, total + 1) :
        s += (1 / (i ** 2))
    return s

print(help(100))

j = 1

waarde = abs(help(j) - pow(pi, 2) / 6)
while waarde > 1 / 100:
    j += 1
    waarde = abs(help(j) - pow(pi, 2) / 6)

print(j)