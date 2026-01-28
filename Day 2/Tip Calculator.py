print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill = bill + bill * tip_percent/100
guests = input("How many people to split the bill?")
print("Each person should pay:", round(bill/int(guests), 2))
