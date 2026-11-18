'''Extend 'password_checker.py' with a for loop over the password that counts digits,
 uppercase letters, lowercase letters and special characters (anything else), using `isdigit()`, 
 `isupper()` and `islower()`. For 'Tops@2026' the counts must be 4, 1, 3 and 1. 
 Print all four counts. '''


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
print("Digits:", digits)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Special characters:", special)
