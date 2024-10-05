def dubbel(getallen) :
    s = set()
    for getal in getallen :
        if getal in s :
            return getal
        else :
            s.add(getal)
    return None

def dubbels(getallen) :
    freq = {}

    for getal in getallen :
        freq[getal] = freq.get(getal, 0) + 1
    return ({key for key, value in freq.items() if value == 1}, {key for key, value in freq.items() if value > 1})