'''Add a second list of 8 prices in ₹ (each between 15 and 120) to 'canteen_menu.py' and use a for loop to
 add up all the prices and count how many dishes cost more than ₹60, then print both numbers. Hint: Create
 `total = 0` and `costly_count = 0` before the loop.'''


for day in range(1, 7):
    discount = 10 + (day - 1) * 5
    print("Day " + str(day) + ": Rs." + str(discount) + " off")
