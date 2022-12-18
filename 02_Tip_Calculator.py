from operator import is_

is_on = True
while is_on:
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? (10, 12, or 15?) "))
    people = int(input("How many people to split the bill? "))

    if tip == 10 or tip == 12 or tip == 15:
        tip_as_percent = tip / 100
        total_tip_amount = bill * tip_as_percent
        total_bill = bill + total_tip_amount
        bill_per_person = total_bill / people
        final_amount = round(bill_per_person, 2)
        print(f"Each person should pay: ${final_amount}")
        if input("Stop this Tip Calculator('y' or 'n'): ") == 'y':
            is_on = False
    else:
        print("Please enter required tip. Try again!")
