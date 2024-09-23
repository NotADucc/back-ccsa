startUur = int(input())
startMin = int(input())
eindUur = int(input())
eindMin = int(input())

if startUur < 18 or eindUur < 18 or (eindUur == 0 and eindMin > 0) or eindUur < startUur or (startUur == eindUur and startMin > eindMin) :
    print("ongeldige invoer")
else :
    totalPrice = 0.0
    deltaStartUurMinWage = min(21, eindUur) - startUur
    deltaStartMinMinWage = (min(30, eindMin) if eindUur == 21 else (30 if eindUur > 21 else eindMin)) - startMin
    deltaUur = eindUur - startUur
    deltaMin = eindMin - startMin
    if deltaStartMinMinWage < 0 :
        deltaStartMinMinWage += 60
        deltaStartUurMinWage -= 1

    if deltaMin < 0 :
        deltaMin += 60
        deltaUur -= 1 
    totalMin = deltaUur * 60 + deltaMin
    
    if deltaStartUurMinWage >= 0 :
        lowMins = deltaStartUurMinWage * 60 + deltaStartMinMinWage
        totalPrice += lowMins * 2
        totalMin -= lowMins
    totalPrice += totalMin * 4
    
    print(totalPrice / 60)



