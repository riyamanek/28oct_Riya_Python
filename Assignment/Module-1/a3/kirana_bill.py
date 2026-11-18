''' Write 'kirana_bill.py' that asks for a customer name, an item name, the quantity bought
 and the price per unit, and prints one line with the customer, item and quantity. 
 Store the quantity using `int()` and the price using `float()`. 
 Hint: `input()` always returns text, so convert before doing any arithmetic.
 Constraint: Do not use if/else; it is not taught yet.'''


name=input("Enter Customer Name:- ")
itemname=input("Enter Item Name:- ")
quantity=int(input("Enter a quantity:- "))
price=float(input("Enter a Price:- "))

print("CustomerName:- ",name)
print("ItemName:- ",itemname)
print("Quantity:- ",quantity)
print("Price:- ",price)
