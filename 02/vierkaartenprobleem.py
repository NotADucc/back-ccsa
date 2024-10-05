isKleur = True if input() == "kleur" else False
waarde = input() if isKleur else int(input())
draaien = True if input() == "ja" else False

output = ""

if isKleur :
    if waarde == "rood" :
        output = "Juist: kaarten met kleur rood moeten niet gedraaid worden." if not draaien else "Fout: kaarten met kleur rood moeten niet gedraaid worden."
    else :
        output = "Juist: kaarten met kleur " + waarde + " moeten gedraaid worden." if draaien else "Fout: kaarten met kleur " + waarde + " moeten gedraaid worden."
else:
    if (waarde & 1) == 0 :
        output = "Juist: kaarten met waarde " + str(waarde) + " moeten gedraaid worden." if draaien else "Fout: kaarten met waarde " + str(waarde) + " moeten gedraaid worden."
    else:
        output = "Juist: kaarten met waarde " + str(waarde) + " moeten niet gedraaid worden." if not draaien else "Fout: kaarten met waarde " + str(waarde) + " moeten niet gedraaid worden."

print(output)