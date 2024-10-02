def omgekeerd(dct) :
    output = {}
    for k, v in dct.items() :
        output[v] = k
    return output

def code39(payload, dct) :
    output = ""
    for ch in payload :
        output += 's' + dct[ch.upper()]

    return output[1:]

def decode39(payload, dct) :
    dct = omgekeerd(dct)
    output = ''
    for i in range(0, len(payload), 10) :
        output += dct[payload[i:i+9]]
    return output