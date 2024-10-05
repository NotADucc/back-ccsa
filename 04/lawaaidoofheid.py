def maximale_blootstelling(decibel) :
    if decibel < 80 :
        return -1.0

    base = 8 * 60 * 60
    decibel -= 80
    decibel //= 3
    return base / (2 ** decibel)