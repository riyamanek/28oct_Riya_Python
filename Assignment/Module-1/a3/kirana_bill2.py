''' Extend 'kirana_bill.py' to calculate the item amount (quantity times price), 
GST at a fixed 5 percent, and the final total, and print each on its own line, for example 'GST
(5%): ₹9.1', joining text and numbers with `str()` and the + sign. Test with 4 units at ₹45.50. 
Hint: Calculate GST as `amount * 5 / 100`.'''


name=input("Enter Customer Name:- ")
itemname=input("Enter Item Name:- ")
quantity=int(input("Enter a quantity:- "))
price=float(input("Enter a Price:- "))

amount=quantity*price
Gst=amount*5/100
Total=amount+Gst

print("CustomerName:- ",name)
print("ItemName:- ",itemname)
print("Quantity:- ",quantity)
print("Price:- ",price)
print(f"Item Amount :- ₹{amount}")
print(f"GST(5%):- ₹{Gst}")
print(f"Total Amount:- ₹{Total}")
