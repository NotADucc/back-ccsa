# Iter
def ggd(g1, g2) :
    (a, b) = (g1, g2) if g1 > g2 else (g2, g1)
    while b != 0 :
        (a, b) = (b, a % b)
    return a
    
# Rec
def ggd(g1, g2) :
    (a, b) = (g1, g2) if g1 > g2 else (g2, g1)
    return rec(a, b)

def rec(a, b) :
    return a if not b else ggd(b, a % b)