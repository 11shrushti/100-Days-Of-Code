# Tip Calculator
print("Welcome to the tip calculator")
bill=(int((input("What was the total bill\n"))))

percentage=(int(input("What percentage tip you would like to pay? 10,12 or 15?\n ")))

people=(int(input("How many people to split the bill?\n")))

split= ((bill/people)*percentage/100)
print(f"Each person should pay {split}")