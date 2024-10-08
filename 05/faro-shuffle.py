def nieuw_kaartspel(kleuren, waarden) :
    lst = []
    for kleur in kleuren :
        for waarde in waarden :
            lst.append(f'{kleur}{waarde}')
    return lst

def splits_kaartspel(kaarten) :
    if len(kaarten) == 1 :
        return ([], kaarten)
    half = len(kaarten) // 2
    return (kaarten[0:half], kaarten[half:])

def faro_shuffle(kaarten_1, kaarten_2) :
    l, r = 0, 0
    lst = []
    while l < len(kaarten_1) :
        lst.append(kaarten_1[l])
        lst.append(kaarten_2[r])
        l += 1
        r += 1
    while r < len(kaarten_2) :
        lst.append(kaarten_2[r])
        r += 1
    return lst
