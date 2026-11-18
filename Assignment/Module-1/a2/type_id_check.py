'''Write 'type_id_check.py' that stores a fee (int), a rate (float), a gym name (str), 
an open flag (bool), a list of 3 workouts and a dictionary with a trainer's name and age, 
then prints the `type()` of each with a label. Then set `fee_copy = fee`, print `id(fee)` 
and `id(fee_copy)`, change `fee_copy` to a new value and print both ids again. '''


fee=1000
rate=4.5
gym_name='Yogata Fitness'
flag=True

workout=["Yoga","Cardio","Running"]

trainer={"name":"Amit","Age":20}

print("Fee:-",type(fee))
print("Rate:-",type(rate))
print("Gym_name:-",type(gym_name))
print("Flag:-",type(flag))
print("Workout:-",type(workout))
print("Trainer:-",type(trainer))

fee_copy=fee
print("id",fee_copy)
