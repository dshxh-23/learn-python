# DICTIONARIES
# Dictionaries are key value pairs, where we may use a key to retrieve it's value.
print('')

student = {'name': 'John',
           'age': 17,
           'courses': ['pps', 'eee', 'evs', 'maths']}

print('Dictionary: ', student)  # printing the entire dictionary.
print('')

# Printing valus to particular keys
print(student['name'])
print(student['courses'])   # returns an error if the key is not found
print('')

# In order to return NONE if the key's not found, use get (an alternative)
print(student.get('age'))
print(student.get('phone'))                 # if no such key exists, returns the <None> by default.
print(student.get('id', 'No such key'))     # if no such key exists, returns the 2nd argument.
print('')

# Modifing dictionaries
student['phone'] = '555-5555-555'       # adds another key to the dictionary.
student['name'] = 'Jane'                # modifies student name.
print(student)
print('')

# To modify multiple keys at ones
student.update({'name': 'ricky', 'phone': '777-8888-777', 'class': 11})
print(student)
print('')

# To delete a key
del student['age']              # Method 1: Use the del keyword.
phone = student.pop('phone')    # Method 2: Use pop to store the deleted key in a variable.
print(student)
print('')

# To check the no. of keys in a dictionary
print(len(student))
print(student.keys())   # to see all the keys
print(student.values()) # to see all values
print(student.items())  # to see keys along with values 
print('')

# Looping through dictionary
for key, value in student.items():
    print(key, value)
print('')