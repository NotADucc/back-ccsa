def letterfrequenties(payload) :
    dct = {}
    for ch in payload :
        if not ch.isalpha() :
            continue
        ch = ch.lower()
        dct[ch] = dct.get(ch, 0) + 1
    return dct

def letterposities(payload) :
    dct = {}
    for i in range(len(payload)) :
        ch = payload[i].lower()
        if not ch.isalpha() :
            continue
        dct[ch] = dct.get(ch, set())
        dct[ch].add(i)
    return dct