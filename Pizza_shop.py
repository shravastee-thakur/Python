print("--------------------------------")
print("\tWelcome to My Pizza Shop!")
print("--------------------------------")

print('''press 1 for small pizza - Rs 100
press 2 for medium pizza - Rs 200
press 3 for large pizza - Rs 300''')

pizza_size = int(input("What kind of Pizza would you like?"))
total_bill = 0

if pizza_size == 1:
    total_bill = 100
    print("Your bill is Rs 100")
if pizza_size == 2:
    total_bill = 200
    print("Your bill is Rs 200")
if pizza_size == 3:
    total_bill = 300
    print("Your bill is Rs 300")

toppings = input("Do you want pepperoni? y / n")
if toppings == "y" or toppings == "Y":
    if pizza_size == 2 or pizza_size == 3:
        total_bill = total_bill + 50
        print(f"Your total bill is Rs {total_bill}")
    else:
        total_bill = total_bill + 30
        print(f"Your total bill is Rs {total_bill}")

if toppings == "n" or toppings == "N":
    total_bill = total_bill
    print(f"Your total bill is Rs {total_bill}")

extra_cheese = input("Do you want extra cheese? y / n")
if extra_cheese == "y" or extra_cheese == "Y":
    total_bill = total_bill + 20
    print(f"Your total bill is Rs {total_bill}")

if extra_cheese == "n" or extra_cheese == "N":
    total_bill = total_bill
    print(f"Your total bill is Rs {total_bill}")

paid_amount = int(input("Please enter the amount paid: "))
if paid_amount > total_bill:
    refund = paid_amount - total_bill
    print(f"Please collect your refund amount Rs {refund}")
if paid_amount < total_bill:
    balance = total_bill - paid_amount
    print(f"Please pay the balance amount Rs {balance}")

print("Thank You! Visit again!")
