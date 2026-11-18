''' Add a second list of 8 prices in ₹ (each between 15 and 120) to 'canteen_menu.py' and use a for loop to 
add up all the prices and count how many dishes cost more than ₹60, then print both numbers. Hint: Create `total = 0`
and `costly_count = 0` before the loop.'''

prices = [40, 80, 50, 100, 90, 45, 60, 75]
total = 0
costly_count = 0
for price in prices:
    total = total + price
    if price > 60:
        costly_count = costly_count + 1
print("Total Price:", total)
print("Dishes costing more than Rs.60:", costly_count)
