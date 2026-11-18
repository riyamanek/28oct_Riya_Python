'''Write 'fest_banner.py' that asks for a number of rows between 1 and 8 and uses while loops 
only to print a right-angled star triangle, followed by an inverted star triangle with the same 
number of rows. Test with 4 rows and paste both triangles as a comment at the end of the file. 
Hint: `print("*", end="")` stays on the same line; a plain `print()` moves to the next line. '''

rows = int(input("Enter number of rows: "))

while rows < 1 or rows > 8:
    rows = int(input("Enter rows: "))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1
i = rows
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i - 1


