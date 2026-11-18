distance=float(input("Enter Your Journey Distance:- "))
Travelclass=input("Enter your travel class(SL,3A,2A):- ")

if(Travelclass=="SL"):
    fare=distance*0.80
    print("Fare:-  ₹",fare)
elif(Travelclass=="3A"):
    fare=distance*2.10 
    print("Fare:-  ₹",fare)
elif(Travelclass=="2A"):
    fare=distance*3.00
    print("Fare:-  ₹",fare)
else:
    print("Invalid")
