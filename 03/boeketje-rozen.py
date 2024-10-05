rood_wit = int(input())
wit_blauw = int(input())
# bepaald of blauw + rood groter/kleiner is dan wit + blauw
groter_dan = True if input() == '>' else False

blauw = 0
wit = 0
rood = 0

for w in range(rood_wit + 1):
    wit = w
    rood = rood_wit - wit
    blauw = wit_blauw - wit
   
    if rood > 1 and blauw > 1 and wit > 1: 
        if groter_dan and (blauw + rood > wit + blauw):
            break
        elif not groter_dan and (blauw + rood < wit + blauw):
            break
    

print(blauw)
print(wit)
print(rood)
