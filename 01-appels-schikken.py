num = int(input())

pallet = int(num / 20 / 35)
num = num % (20 * 35)
kisten = int(num / 20)
num = num % 20
print(pallet)
print(kisten)
print(num)