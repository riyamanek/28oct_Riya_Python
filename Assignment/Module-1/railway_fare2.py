distance=float(input("Enter Your Journey Distance:- "))
Travelclass=input("Enter your travel class(SL,3A,2A):- ")
age=int(input("Enter your Passenger Age:- "))

if(Travelclass=="SL"):
    fare=distance*0.80
    if(age>=60):
        concession=fare*40/100
    elif(age<12):
        concession=fare*50/100
    else:
        concession=0
    final_fare=fare-concession
    print("Fare: ₹", fare)
    print("Concession: ₹", concession)
    print("Final Fare: ₹", final_fare)                

    
elif(Travelclass=="3A"):
    fare=distance*2.10 
    concession=0
    final_fare=fare-concession
    print("Fare: ₹", fare)
    print("Concession: ₹", concession)
    print("Final Fare: ₹", final_fare)                
    

   
elif(Travelclass=="2A"):
    fare=distance*3.00
    concession=0
    final_fare=fare-concession
    print("Fare: ₹", fare)
    print("Concession: ₹", concession)
    print("Final Fare: ₹", final_fare)                
    


    
else:
    print("Invalid")
