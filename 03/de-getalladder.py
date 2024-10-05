num = int(input())

for i in range(0, num + 1, 1) :
    for j in range(0, i, 1) :
        print(j + 1, end = "")
    if i > 0 :
        print()