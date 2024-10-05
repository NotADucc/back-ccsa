ans = 0
while True :
    inp = int(input())
    if not inp :
        break
    ans += inp
    if ans == 21 or ans > 21 :
        break

message = "Verbrand ("+ str(ans) +")" if ans > 21 else "Gewonnen!" if ans == 21 else "Voorzichtig gespeeld ("+ str(ans) +")"

print(message)