''' 
Arithmetic Operators:-

Addition:                               +
Subtraction:                            -
Multiplication:                         *
Division:                               /
Floor Division (drops decimal):         //
Exponent:                               **      
Modulus (gives remainder):              %          

NOTE: All operators, except exponent, are evaluated from left to right {6/2/3 = (6/2)/3 = 1}. Exponent operator is evaluated from right to left {2**2**3 = 2**8 = 256}.

Boolean Operators (for comparision):-

Equal:                          ==
Not Equal:                      !=
Greater Than:                   >
Less Than:                      <
Greater or Equal:               >=
Less or Equal:                  <=
'''

print('')

# Numeric data types
integer = 3
float = 3.14
complex = 5+1j      # j is used to denote the imaginary part (instead of iota) in complex data type
print(type(integer), type(float), type(complex))
print('')

# Adding numeric data types
print(integer + complex + float)
print('')

# Some methods
print(round(34.74942))          # rounds to nearest integer.
print(round(34.74942, 2))       # 2nd argument specifies how many decimal points we want to round it.
print('')

# Operators to return booleans
print(integer == float)             # returns False
print(integer == round(float))      # returns True
print('')

# Casting (changing 1 data type to other)

num1 = '12'
num2 = '18'

print(int(num1) + int(num2))
print('')

# Concatenating integer and string
x = 3
y = "john"
print(x, y)     # you can't concatenate a string and an integer using '+' symbol. Using ',' to concatenate adds a space after each variable.
