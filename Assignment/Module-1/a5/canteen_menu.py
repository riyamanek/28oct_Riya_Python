''' Write 'canteen_menu.py' with a list of 8 dish names for a fictional college canteen and use a for loop with a counter variable to 
print the menu as '1. Veg Sandwich', '2. Masala Dosa' and so on. Hint: Set `count = 0` before the loop and add 1 inside it; 
join text with `str(count)`. Constraint: Do not use list indexing or `enumerate()`.'''

dishes=["Veg Sandwich",
        "Masala Dosa",
        "Pav Bhaji",
        "Veg Pizza",
        "Cheese Burger",
        "Idli Sambhar",
        "French Fries",
        "Paneer Roll"]

count=0
for dish in dishes:
    count=count+1
    print(str(count)+"."+dish)