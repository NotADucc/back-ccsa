aantal_piraten = int(input())
aantal_noten = int(input())

for i in range(aantal_piraten) :
    deling = aantal_noten // aantal_piraten
    rest = aantal_noten % aantal_piraten
    prefix_noot = ' noot' if deling == 1 else ' noten'
    prefix = str(aantal_noten) + ' noten = ' + str(deling) + prefix_noot + ' voor piraat#' + str(i + 1) + ' en '
    suffix = str(rest) if rest != 0 else 'geen'
    apen_noot = ' noot' if rest == 1 else ' noten'
    print(prefix + suffix + apen_noot + ' voor de aap')
    aantal_noten = aantal_noten - deling - rest

deling = aantal_noten // aantal_piraten
rest = aantal_noten % aantal_piraten
prefix_noot = ' noot' if deling == 1 else ' noten'
prefix = 'elke piraat krijgt ' + str(deling) + prefix_noot + ' en '
suffix = str(rest) if rest != 0 else 'geen'
apen_noot = ' noot' if rest == 1 else ' noten'
print(prefix + suffix + apen_noot + ' voor de aap')