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
