def bubble_sort(a):
    length = len(a)
    counter = 0
    for i in range(length - 1) :
        for j in range(length - 1, i, -1) :
            counter += 1
            if a[j - 1] > a[j] :
                a[j] ^= a[j - 1]
                a[j - 1] ^= a[j]
                a[j] ^= a[j - 1]
            
        print(a)  
    print("Voor een rij van lengte " + str(length) + " werd het if-statement " + str(counter) + " keer uitgevoerd")

a = [int(_) for _ in input().split()]
bubble_sort(a)

