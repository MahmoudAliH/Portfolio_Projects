print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? "))
nbr_pers = int(input("How many people to split the bill?"))

Thus_everyone = round(total_bill/nbr_pers, 2)

if tip == 10:
  total = str(round(Thus_everyone*1.10, 2))
  print(type(total))
  print("Each person should pay: $"+total)
elif tip==12:
  total = str(round(Thus_everyone*1.12, 2))
  print("Each person should pay: $"+total)
elif tip==15:
  total = str(round(Thus_everyone*1.15, 2))
  print("Each person should pay: $"+total)
else:
  print(f"Each person should pay: ${Thus_everyone}")