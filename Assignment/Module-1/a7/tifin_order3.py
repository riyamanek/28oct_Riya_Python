''' Add a kitchen capacity limit of 20 tiffins to 'tiffin_orders.py': as soon as the running 
total of tiffins reaches or goes above 20, print 'Kitchen full' and leave the loop with `break`. 
Test with three orders of 8, 7 and 9 tiffins on plan 1.'''


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
    if total_tiffins >= 20:
        print("Kitchen full")
        break
print("Total Tiffins Ordered:", total_tiffins)
print("Total Bill: ₹", total_bill)
