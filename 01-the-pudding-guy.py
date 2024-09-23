count = int(input())
price = float(input())
codes = int(input())
miles = int(input())

print("Phillips spendeerde $" + str(count * price) + " voor " + str(int(count / codes) * miles) + " frequent flyer mijlen.")