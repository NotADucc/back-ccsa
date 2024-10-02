def codeer(tekst, sleutel) :
    func = lambda x, y: x + y
    return c(tekst, sleutel, func)


def decodeer(tekst, sleutel) :
    func = lambda x, y: x - y
    return c(tekst, sleutel, func)
    
def c(tekst, sleutel, lamb) :
    s_n = len(sleutel)
    output = ''
    for i in range(len(tekst)) :
        ch = tekst[i]
        if not ch.isalpha() or ch.islower() :
            output += ch
            continue
        s_i = i % s_n
        output += chr(lamb(ord(ch) - ord('A'), ord(sleutel[s_i]) - ord('A')) % 26 + ord('A'))
    return output
