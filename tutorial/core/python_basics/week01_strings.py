print('')       # for empty line

greeting = 'Hello'
name = 'Michel'
msg1 = greeting + ', ' + name

print(msg1)
print('')

# string can also be treated as an array.
print(len(msg1))    # For length of msg1
print(name[2])      # For printing chr at index 2
print(msg1[2:6])    # For printing chrs from (including) index 2 and till (EXCLUDING) 6
print(msg1[4:])     # Slicing - for printing chrs from index 4 onwards
print('')

# methods for string. Documentation: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
print(msg1.lower())         # Converts the str to lowercase
print(msg1.upper())         # Converts the string to uppercase
print(msg1.count('l'))      # counts no. of times 'l' appears in msg1
print(msg1.find('che'))     # returns the index from which 'che' starts. Returns -1 if the str does not exist.
print('')

msg2 = msg1.replace('Michel', 'Steve')      # returns string in which argument 2 is present instead of argument 1. 
print(msg2)
print('')

# String concatenation
str1 = "Hello"
str2 = "World"
msg3 = str1 + ", " + str2 + ". Welcome!"
print(msg3)

# Using formatted string for string concatenation.
msg4 = '{}, {}! How u doin?'.format(str1, str2)     # Use placeholders instead of vars & write the var names as arguments to format method.
print(msg4)

# Using f strings - The best method of string concatenation. Just add an f before the string and now you can write var names inside of placeholders.
msg5 = f'{str1}, {str2}! I\'m {name.upper()}. U\'all are welcome here!'  # Used \ so string doesn't end upon encountering <'>.
print(msg5)
print('')

# Multiline strings are represented by 3 apostrpys. They can also be used as comments cuz they are ignored if not assigned to a variable.
a = '''this is
a
multiline string.
'''
print(a + ' hello \'Michel\'.\tI am Jackson')
print('')

# Escape sequences for strings
'''
\' --> '
\' --> "
\\ --> \ 
\t --> horizontal tab
\b --> backspace
\n --> new line
'''


# print(dir(var_name)) --> shows all possible attributes and methods we have access to for that variable.
# print(help(data_type)) --> Gives information of all possible attributes and methods we have access to for that data type.