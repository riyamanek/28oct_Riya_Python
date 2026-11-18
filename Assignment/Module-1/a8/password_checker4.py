''' >Finish 'password_checker.py' by printing a masked version that keeps the first 2 and last 2 
characters and replaces the middle with stars, so 'Tops@2026' shows as 'To*****26'. 
Run the program for 'Tops@2026', 'tops2026' and 'abcde', and paste the outputs as a comment 
at the end of the file. Hint: Repeat a star with `"*" * 5`; use slices for the first and last 2
 characters'''


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
print("Password length:", length)
print("First character:", password[0])
print("Last character:", password[-1])
print("Password backwards:", password[::-1])
print("Digits:", digits)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Special characters:", special)
if length >= 8 and digits >= 1 and uppercase >= 1 and lowercase >= 1 and special >= 1:
    print("Password Strength: Strong")
elif length >= 6 and digits >= 1 and (uppercase + lowercase) >= 1:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
masked = password[:2] + "*" * (length - 4) + password[-2:]
print("Masked password:", masked)




