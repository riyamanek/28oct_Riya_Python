'''Write 'fest_gate.py' that uses a while loop to keep asking for visitor names at the gate of
 a fictional college fest until the user types 'done', then prints how many visitors entered, 
 not counting 'done'. Hint: Ask for the first name before the loop and ask again at the end of 
 each round. Constraint: Do not use break; it is taught later. '''

count = 0
name = input("Enter visitor name (type done to stop): ")
while name != "done":
    count = count + 1
    name = input("Enter visitor name (type done to stop): ")
print("Total visitors entered:", count)