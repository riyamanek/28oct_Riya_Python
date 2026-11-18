'''Make 'railway_fare.py' reject bad input by printing a clear error message instead of a fare when
 the distance is zero or negative, the distance is above 3000 km, or the age is below 1 or above 
 120. Constraint: Use only if/elif/else; do not use try/except.'''


distance=float(input("Enter Your Journey Distance:- "))
Travelclass=input("Enter your travel class(SL,3A,2A):- ")
age=int(input("Enter your Passenger Age:- "))

if(distance<=0):
    print("Distance must be greater than 0.")
elif(distance>3000):
    print("Distance cannot be above 3000km")
elif(age<1 or age>120):
    print("age between 1 to 120")
elif(Travelclass=="SL"):
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

