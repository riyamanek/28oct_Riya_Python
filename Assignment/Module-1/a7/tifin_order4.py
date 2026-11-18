''' Finish 'tiffin_orders.py' by adding a bulk-discount branch `if tiffins >= 10:` whose body is
 only `pass` with the comment '# bulk discount to be added later'. Then run it with Asha
 (plan 1, 3 tiffins), Ravi (plan 9), Mehul (plan 2, 12 tiffins) and 'stop', and paste the
 output as a comment at the end of the file.'''


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
    if tiffins >= 10:
        pass  
    total_tiffins = total_tiffins + tiffins
    total_bill = total_bill + bill
    if total_tiffins >= 20:
        print("Kitchen full")
        break
print("Total Tiffins Ordered:", total_tiffins)
print("Total Bill: ₹", total_bill)


