#=== MAP FUNCTION ===#

"""
The map method <map(function_name, sequence_variable)> is used to apply some function to every element of a sequence like list or tuples.
"""

def yell(*words):
    uppercased = map(str.upper, words)      # Note: we need to pass the function object, and not call the function using ()
    print(*uppercased)


#=== LIST COMPREHENSIONS ===#
"""
List comprehensions can construct lists using basic logic in a single line
"""

def yell_v2(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


#=== FILTER ===#
"""
Used to filter elements from a sequence (like lists and dictionary).
Similar to map, but here, the 1st argument is a function that returns a boolean value, determining if the element is to be filtered out or not.
"""

def yelled_words(*words):
    return list(filter(str.isupper, words))

print(yelled_words("Mike", "HARRY", "JOHN", "Peter", "TONY"))


#=== DICTIONERY COMPREHENSIONS ===#
"""
Similar to list comprehensions, used to make dictionaries in 1 line
"""

students = ["Hermione", "Harry", "Ron"]
gryffindors = []

# method 1: traditional method
for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

# method 2: using list comprehensions
gryffindors_v2 = [{"name": student, "house": "Gryffindor"} for student in students]

# method 3: using dictionary comprehensions
gryffindors_v3 = {student: "Gryffindor" for student in students}