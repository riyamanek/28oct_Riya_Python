''' Finish 'canteen_menu.py' with a for loop over a canteen board name you invent
 (at least 15 characters, with spaces) that counts the vowels and the spaces, and prints
   both counts. Run the whole program and paste its output as a comment at the end of the file. 
   Hint: Test each letter with `if letter in "aeiouAEIOU":'''


board_name = "Darshan College Canteen"
vowel_count = 0
space_count = 0
for letter in board_name:
    if letter in "aeiouAEIOU":
        vowel_count = vowel_count + 1
    if letter == " ":
        space_count = space_count + 1
print("Canteen Board:", board_name)
print("Total Vowels:", vowel_count)
print("Total Spaces:", space_count)

