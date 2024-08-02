bill = input("How much is the bill? ")
num_people = input("How many people are paying? ")
tip_percent = input("How much would like to tip? ")

divided_bill = float(bill) / int(num_people)

tip_amount = round(divided_bill, 2) * (int(tip_percent) / 100)
total_bill = tip_amount + divided_bill
total_bill = "{:.2f}".format(total_bill)

print(f"Each person owes ${total_bill} with tip.")
