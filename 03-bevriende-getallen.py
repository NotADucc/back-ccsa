a, b = int(input()), int(input())

som_a, som_b = 0, 0

for i in range(1, a + 1 // 2, 1) :
    if a // i == a / i :
        som_a += i
for i in range(1, b + 1 // 2, 1) :
    if b // i == b / i :
        som_b += i

output = ' ' if som_a == b and som_b == a else ' geen '
print(f'{a} en {b} zijn{output}bevriende getallen')