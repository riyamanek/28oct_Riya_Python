''' Create 'fix_infinite.py' with these lines: `tokens = 5`, `while tokens > 0:` and an indented 
`print("Token left:", tokens)`. Run it, stop it with Ctrl+C in the terminal, then fix the loop so
 it prints tokens 5 down to 1 and ends by itself. Hint: A while loop needs a line inside it that 
 changes the variable used in its condition.'''

tokens = 5
while tokens > 0:
    print("Token left:", tokens)
    tokens = tokens - 1