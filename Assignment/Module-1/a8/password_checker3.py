''' Add a strength rating to 'password_checker.py' using if-elif-else: 'Strong' if the length is
 8 or more and every one of the four counts is at least 1, 'Medium' if the length is 6 or more 
 with at least one digit and one letter, otherwise 'Weak'. Test with 'Tops@2026', 'tops2026' and
   'abcde'.'''


password = input("Enter password: ")
digits = 0
uppercase = 0
lowercase = 0
special = 0
for ch in password:
    if ch.isdigit():
        digits += 1
    elif ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    else:
        special += 1
length = len(password)
if length >= 8 and digits >= 1 and uppercase >= 1 and lowercase >= 1 and special >= 1:
    print("Password Strength: Strong")
elif length >= 6 and digits >= 1 and (uppercase + lowercase) >= 1:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
