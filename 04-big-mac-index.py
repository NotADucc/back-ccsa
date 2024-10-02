def waardering(g1, g2) :
    v = ((g1 / 4.07)- g2) / g2 * 100
    if v <= -25 :
        v = 'sterk ondergewaardeerd'
    elif v <= -5 :
        v = 'ondergewaardeerd'
    elif v <= 5 :
        v = 'ongeveer gelijk'
    elif v <= 25 :
        v = 'overgewaardeerd'
    else :
        v = 'sterk overgewaardeerd'
    return v
        

def wisselkoersanalyse(g1, g2) :
    g = g1.split(" ")
    g1 = float(g[0])
    return f'De {' '.join(g[1:])} is {waardering(g1, g2)} ten opzichte van de dollar.'