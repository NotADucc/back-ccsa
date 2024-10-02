num = int(input())

if num.bit_count() == 1 :
    print(0)
else :
    count = 0
    for i in range(1, num, 1) :
        current = 0
        for j in range(i, num, 1) :
            current += j
            if current >= num :
                if current == num :
                    count+=1
                break

    print(count)