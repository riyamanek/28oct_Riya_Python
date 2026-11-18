'''Finish 'kirana_bill.py' by printing the final total again as whole rupees,
 converted with `int()`. Then run it for 4 units at ₹45.50 and for 2 units at ₹150, 
 and paste both bills as a comment at the end of the file. Hint: `int(191.1)` gives 191;
 it cuts the decimal part and does not round.'''


name=input("Enter Customer Name:- ")
itemname=input("Enter Item Name:- ")
quantity=int(input("Enter a quantity:- "))
price=float(input("Enter a Price:- "))

amount=quantity*price
Gst=amount*5/100
Total=amount+Gst


print("\n-----------\"ALL IN ONE Kirana Store\"----------------")
print("CustomerName:\t",name)
print("ItemName:\t",itemname)
print("Quantity:\t",quantity)
print("Price:\t\t",price,"\n")
print("ItemAmount:\t₹",amount)
print("GST(5%):\t₹",Gst)
print("Total Amount:\t₹",Total)
print("Whole Rupess:\t₹",int(Total))