def vertalingToevoegen(w1, w2, dct) :
    dct[w1] = w2

def vertaling(w1, dct) :
    return dct.get(w1, '???')