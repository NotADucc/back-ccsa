_noten = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
def ontleding(str_noot) : 
    if len(str_noot) == 1 :
        return (str_noot, '')
    if str_noot[0:2] in _noten :
        return (str_noot[0:2], str_noot[2:])
    return (str_noot[0:1], str_noot[1:])

def noten(grond, toon_intervallen) :
    output = []
    grond_index = _noten.index(grond)
    for interval in toon_intervallen :
        index = (grond_index + interval) % 12
        output.append(_noten[index])
    return output

def akkoord(str_noten, types, symbolen) :
    ont = ontleding(str_noten)
    return tuple(noten(ont[0], types[symbolen[ont[1]]]))
