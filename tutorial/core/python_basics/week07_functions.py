### FUNCTIONS

# Empty function for later use
def emptyFunc():   # def stands for defination
    pass        # pass tells the interpreter that this func currently has no code in it but the code will be added so that id doesn't throw in any error.

# Function which returns a string.
def greeting(name):
    return f'Hello {name}!'

print()
print(greeting('Jack').upper())    # Jack is passed as an argument here. We can also use methods on the returned value.
print()

def intro(name, age, city='India'): # Default value for parameter 3. If parameter 3 is not specified, it will take the default value.
    return f'I am {name}. I am {age} years old. I\'m from {city}.'

print(intro('Michel', 17,))
print()