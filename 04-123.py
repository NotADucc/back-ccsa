def even_oneven(getal):
    even = 0
    oneven = 0
    while getal > 0 :
        g = getal % 10
        getal //= 10
        if (g % 2) == 1 :
            oneven += 1
        else :
            even += 1
    return (even, oneven)

def volgende(getal):
    if getal == 0 :
        return 101
    (even, oneven) = even_oneven(getal)
    total = 0
    while getal > 0 :
        total += 1
        getal //= 10
    return int(f'{even}{oneven}{total}')

def stappen(getal):
    if getal == 123 :
        return 0
        
    i = 1
    while volgende(getal) != 123 :
        getal = volgende(getal)
        i += 1
    return i

if __name__ == '__main__':
    import doctest
    doctest.testmod()
