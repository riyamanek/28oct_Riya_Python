''' Add a volunteer code check at the start of 'fest_gate.py': give 3 attempts to enter 
the secret code 'FEST26' using a while loop with an `attempts` counter, and print 'Gate 
unlocked' or 'Locked after 3 wrong attempts'. Hint: Keep a flag `unlocked = False` and stop
 the loop when it becomes True or attempts reach 3. Constraint: Do not use break.'''

attempts = 0
unlocked = False
while attempts < 3 and unlocked == False:
    code = input("Enter volunteer code: ")
    attempts = attempts + 1
    if code == "FEST26":
        unlocked = True
        print("Gate unlocked")
if unlocked == False:
    print("Locked after 3 wrong attempts")