weekly = int(input ("How many times a week do you eat at the student cafeteria?"))
price = float(input ("the price of the typcal lunch?"))
groceries = float(input ("How much money do you spend on groceries in a week?"))
print ("Average food expenditure:")
weekly_sum = weekly*price+groceries
Daily_sum = weekly_sum/7
print ("Daily:",Daily_sum, "euros")
print ("Weekly:",weekly_sum, "euros")


