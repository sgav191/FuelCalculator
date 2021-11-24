"""
To add time delays in this project
"""
import time
from decimal import Decimal, ROUND_DOWN
fuelregions = ["1: London","2: Northern Ireland","3: Wales","4: Scotland","5: South West","6: South East","7: East of England","8: East Midlands","9: West Midlands","10: Yorkshire and the Humber","11: North East","12: North West"]
fuelprices = [[142,145],[140,142],[141,145],[141,145],[142,145],[142,146],[142,145],[141,145],[141,145],[141,145],[140,144],[141,145]]

print ("Hello and welcome to FUELCALC-2.0!")
time.sleep(1)
print ("With this groundbreaking utility, you can calculate the approximate amount you'll have to pay for fuel in your area.")
input("Press enter when you are ready to continue and see your options...")
for i in fuelregions:
    print (i)
    time.sleep(0.25)
userregionchoice = int(input ("Please type in the number of your region here: "))
userregionchoice = userregionchoice-1
print ("What type of fuel does your car use?")
print ("""Choose from the list:
1: Unleaded
2: Diesel
3: Super Unleaded
""")
userfuelchoice = int(input ("Please type your answer here: "))
userfuelchoice = userfuelchoice-1
userfuelrate = fuelprices[userregionchoice][userfuelchoice]
userfuelquantity = int(input ("How much fuel do you want, in litres: "))
userfuelprice = (userfuelrate*userfuelquantity)/100
userfuelprice = Decimal(userfuelprice).quantize(Decimal('.01'), rounding=ROUND_DOWN)
print (f"""Your fuel price is:
£{userfuelprice}""")
