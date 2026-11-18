'''Write 'password_checker.py' that asks for a password and prints its length with `len()`, 
its first character, its last character using index -1, and the password written backwards
 using slicing. Test with 'Tops@2026'. Hint: The slice `text[::-1]` reverses a string. '''


password = input("Enter password: ")
print("Password length:", len(password))
print("First character:", password[0])
print("Last character:", password[-1])
print("Password backwards:", password[::-1])
