''' Extend 'tiffin_orders.py' to ask for a plan number for each order: 1 Regular ₹60,
 2 Jain ₹70, 3 Special ₹90. If the plan number is anything else, print an error and use 
 `continue` so the order is not counted or billed. Keep a running bill and print it at the end.
 '''


total_tiffins = 0
total_bill = 0
while True:
    name = input("Enter customer name: ")
    if name == "stop":
        break
    tiffins = int(input("Enter number of tiffins: "))
    plan = int(input("Enter plan number (1-Regular, 2-Jain, 3-Special): "))
    if plan == 1:
        price = 60
    elif plan == 2:
        price = 70
    elif plan == 3:
        price = 90
    else:
        print("Invalid plan number!")
        continue
    bill = tiffins * price
    total_tiffins = total_tiffins + tiffins
    total_bill = total_bill + bill
print("Total Tiffins Ordered:", total_tiffins)
print("Total Bill: ₹", total_bill)
