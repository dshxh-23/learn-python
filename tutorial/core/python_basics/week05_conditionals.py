# Comparisons:
    # Equal:            ==
    # Not Equal:        !=
    # Greater Than:     >
    # Less Than:        <
    # Greater or Equal: >=
    # Less or Equal:    <=
    # Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# Boolean operations:
    # and
    # or
    # not


# Using if, elif and else
language = 'python'

if language == 'python':
    print('Language is Python')

elif language == 'java':
    print('Language is Java')

else:
    print('No match found.')

# Using boolean operators
user = 'Admin'
status = 'logged out'

if user == 'Admin' and status == 'logged in':
    print('admin page')

elif user != 'Admin' and status == 'logged in':
    print('You are not the admin.')

elif user == 'Admin' and not status == 'logged in':
    print('You need to log in.')

else:
    print('Get lost')

print('')

# IS operator and IDs
a = [1, 2, 3]
b = [1, 2, 3]

print('a == b:', a==b)      # == Checks value
print('a is b:', a is b)    # is cheks id
print('')

print('id of a: ', id(a))   # id can be obtained by id(<var_name>) func.
print('id of b: ', id(b))

b = a       # equating id's of a and b
print('Now, a is b:', a is b)   # so basicaly <a is b> is the same as <id(a) == id(b)>