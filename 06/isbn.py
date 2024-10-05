def overzicht(codes) :
    freq = {}
    land = {
        "0": "Engelstalige landen",
        "1": "Engelstalige landen",
        "2": "Franstalige landen",
        "3": "Duitstalige landen",
        "4": "Japan",
        "5": "Russischtalige landen",
        "7": "China",
        "6": "Overige landen",
        "8": "Overige landen",
        "9": "Overige landen",
    }
    for code in codes :
       if is_geldig(code) :
           land_code = land[code[3]]
           freq[land_code] = freq.get(land_code, 0) + 1
       else :
           freq["Fouten"] = freq.get("Fouten", 0) + 1
    for i in ("0", "2", "3", "4", "5", "7", "8") :
        print(land[i] + ": " + str(freq.get(land[i], 0)))
    print("Fouten: " + str(freq.get("Fouten", 0)))

def is_geldig(code) :
    if len(code) != 13 or code[0:3] not in ("978", "979"):
        return False
    o, e = 0, 0
    for i in range(1, 13, 1) :
        if (i & 1) == 1 :
            o += int(code[i - 1])
        else :
            e += int(code[i - 1])
    c = int(code[12])

    return c == (10 - (o + (3 * e)) % 10) % 10
