print("Welcome to the tip calculator")
bill = int(input("What was your total bill? $"))
tip = int(input("What is your tip % you want to give"))
people = int(input("How many people will split the bill?"))
pay = (bill/people) + bill*tip/100/people
print(f"Each person should pay {pay} $")
