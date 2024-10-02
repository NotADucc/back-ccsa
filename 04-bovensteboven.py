_mirror = {
    '0' : '0',
    '1' : '1',
    # '2' : '5',
    # '5' : '2',
    '6' : '9',
    '8' : '8',
    '9' : '6'
}
def bovensteboven(getal) :
    str_getal = str(getal)
    l, r = 0, len(str_getal) - 1
    while l <= r :
        if str_getal[l] not in _mirror or _mirror[str_getal[l]] != str_getal[r] :
            return False
        l += 1
        r -= 1
    return True
    
def volgende(getal) :
    getal += 1
    while not bovensteboven(getal) :
        getal += 1
    return getal