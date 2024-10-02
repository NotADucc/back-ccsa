def csom(getal) :
    temp = 0
    while getal >= 10 :
        temp += getal % 10
        getal //= 10
        if getal < 10 :
            getal += temp
            temp = 0
    return getal
