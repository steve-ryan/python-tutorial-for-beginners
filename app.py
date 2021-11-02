electricity_bill = float(input("How much for the electricity? "))
water_bill = float(input("How much for the water "))

total_bill = electricity_bill + water_bill
total_bill2 = (electricity_bill + water_bill)*0.75

name = input("What is my name ?")
name2 = input("What is my name ?")

print("%s owe them ksh.%.2f " %(name,total_bill))
print("%s owe them ksh.%.2f " %(name2,total_bill2))