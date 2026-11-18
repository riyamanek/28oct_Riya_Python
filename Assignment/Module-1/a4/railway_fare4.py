'''Finish 'railway_fare.py' so it prints a neat ticket showing class, distance, age, base fare,
 concession and final fare in ₹. Run it for (SL, 250 km, age 65), (SL, 100 km, age 8), 
 (3A, 400 km, age 35), (2A, -50 km, age 30) and (AC, 200 km, age 40), and paste all five outputs as
  a comment at the end of the file.'''


distance = float(input("Enter journey distance in km: "))
travel_class = input("Enter travel class (SL, 3A, 2A): ")
age = int(input("Enter passenger age: "))

if distance <= 0:
    print("Error: Distance must be greater than 0.")

elif distance > 3000:
    print("Error: Distance cannot be above 3000 km.")

elif age < 1 or age > 120:
    print("Error: Age must be between 1 and 120.")

elif travel_class == "SL":
    base_fare = distance * 0.80

    if age >= 60:
        concession = base_fare * 40 / 100
    elif age < 12:
        concession = base_fare * 50 / 100
    else:
        concession = 0

    final_fare = base_fare - concession

elif travel_class == "3A":
    base_fare = distance * 2.10
    concession = 0
    final_fare = base_fare

elif travel_class == "2A":
    base_fare = distance * 3.00
    concession = 0
    final_fare = base_fare

else:
    print("Error: Invalid travel class!")

if distance > 0 and distance <= 3000 and age >= 1 and age <= 120 and (travel_class == "SL" or travel_class == "3A" or travel_class == "2A"):

    print("\n========== RAILWAY TICKET ==========")
    print("Travel Class :", travel_class)
    print("Distance     :", distance, "km")
    print("Passenger Age:", age)
    print("-----------------------------------")
    print("Base Fare    : ₹", round(base_fare))
    print("Concession   : ₹", round(concession))
    print("Final Fare   : ₹", round(final_fare))
    print("===================================")
