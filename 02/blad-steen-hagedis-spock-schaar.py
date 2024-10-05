speler1 = input()
speler2 = input()
if speler1 == speler2 :
    print("gelijkspel")
else :
    winner = ""
    
    if speler1 == "blad" :
        winner = "speler1" if speler2 in { "Spock", "steen" } else "speler2"
    elif speler1 == "steen" :
        winner = "speler1" if speler2 in { "hagedis", "schaar" } else "speler2"
    elif speler1 == "hagedis" :
        winner = "speler1" if speler2 in { "Spock", "blad" } else "speler2"
    elif speler1 == "Spock" :
        winner = "speler1" if speler2 in { "steen", "schaar" } else "speler2"
    else :
        winner = "speler1" if speler2 in { "blad", "hagedis" } else "speler2"
        
    print(winner + " wint")