import math
#ELECRICITY BILL CALCULATOR#
rate = 1
#Name of the customer, ENTRY REQUIRED!!!#
Name=input("Name:")
if Name.strip() == "":
    print("NAME REQUIRED")
else:
    print("That is your name")

#Electricity usage#
rate=int(input("How many Megawatts? "))
if rate=="":
    print("ENTER")
else: print("Great!")

#Time to calculate how much you are paying, 1 megawatt is equal to 10.00 Pesos#
bill=rate*10

print(bill)
print("Pesos")
