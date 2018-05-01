
total_amount = float(input("Enter total amount of check: "))

# convert percentage amount to decimal.
tip_percentage = float(input("Enter tip percentage: "))

#calculate tip rounded to the nearest cent.
total_tip = round(total_amount * tip_percentage, 2)

print(total_tip)