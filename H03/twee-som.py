def twoSum(getallen, doel) :
    # ik ga ervan uit dat het wilt dat ik een O(n^2) algo maak
    dct = {}

    for x in range(len(getallen)) :
        if getallen[x] in dct :
            return (dct[getallen[x]], x)
        else :
            delta = doel - getallen[x]
            dct[delta] = x
    return None

def twoSumHash(getallen, doel) :
    # O(n)
    return twoSum(getallen, doel) 