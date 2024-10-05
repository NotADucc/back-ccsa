def selection_sort_vooraan(a):
    for i in range(len(a) - 1) :
        pos = i
        min = a[i]
        for j in range(i + 1, len(a), 1) :
            if min > a[j] :
                pos = j
                min = a[j]
        a[i], a[pos] = a[pos], a[i]
        print(a)

a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)

