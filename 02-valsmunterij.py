weging1 = input()
weging2 = input()

munt = 0

if weging1 == "links" :
    munt = 4
elif weging1 == "rechts" :
    munt = 1
else : 
    munt = 7

if weging2 == "links" :
    munt += 1
elif weging2 == "evenwicht" :
    munt += 2


print("muntstuk #" + str(munt) + " is vervalst")