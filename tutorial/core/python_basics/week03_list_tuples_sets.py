# LISTS - []

"""
There are 5 data types in python:
Numeric data type:      int, float, complex
Sequence data type:     string, list, tuple, range
Set data type:          set, frozen set
Boolean type:           bool
Mapping type:           dictionary

"""

print('')
courses = ['science', 'commerce', 'arts', 'humanities']

# Timepass
print('Orignal list: ', courses)          # returns entire list.
print('Length of list: ', len(courses))     # returns length of list (here, returns 4).
print('index 0 of list: ', courses[0])       # returns 1st element of list (index 0).
print('last item (index -1) of list: ', courses[-1])      # returns 1st element of the list from the right (index -1).
print('slicing list: ', courses[:2])     # returns a list with elements from 0 untill (but not including) 2 of the orignal list.
print('')

# To add an item at the end of the list
courses.append('journalism')
print('Using append: ', courses)
print('')

# To add an item at a specic posn in a list
courses.insert(4, 'economics')          # 1st argument takes posn, 2nd takes element.
print('Using insert: ', courses)
print('')

# To add a list in a list
courses_2 = ['physics', 'chemistry']
courses.insert(1, courses_2)    # You can also use append to add a list at the end of a list
print('Inserting list in a list: ', courses)
print('')

# To add multiple items in a list
courses_3 = ['entrepreneur', 'buisness analyst']
courses.extend(courses_3)       # adds the argument list (courses_3) at the end of courses.
print('using extend: ', courses)
print('')

# Removing items
courses.remove(['physics', 'chemistry'])        # removing specific elements from the list
print('removing specific elemnts: ', courses)
print('')

# Using pop to remove and store the last item in the list
popped_item = courses.pop()
print('removing last item using pop: ', courses)
print('popped item:', popped_item)
print('')

# Reversing the list
courses.reverse()
print('reversing the list: ', courses)
courses.reverse()   # to get orignal list back
print('')

# Arranging list in alphabetical order
sorted_courses = sorted(courses)    # there is no change in our orignal list.
print('alphabetically ordered list: ', sorted_courses)
print('orignal list: ', courses)
print('')

# Sorting orignal list in alphabetical order and reverse
courses.sort()              # sorts orignal list alphabetically. More convienent if orignal list is not needed.
print('Sorting list alphabetically: ', courses)
courses.sort(reverse=True)  # sorts orignal list reverse alpabetically
print('Sorting list reverse alphabetically: ', courses)
print('')

# Finding index of an item in the list
print('index of humanities: ', courses.index('humanities'))     # value error if the given item is not in the list.
print('')

# Checking if an item exists in a list or not
print('Arts in courses: ', 'arts' in courses) # Returns true if 'arts' is there in the list courses
print('')

# Looping values of the list. Will be explained later.
for index, course in enumerate(courses, start=1):
    print(index, course)    
print('')

# Turning list into string seaperated by a certain values
course_str = ", ".join(courses)
print('string: ', course_str)
print('')

# Turning string back into a list
new_list = course_str.split(", ")
print('new list: ', new_list)
print('')

# Numerical list
nums = [3, 5, 1, 7, 2, 6]
print('List: ', nums)
print('')

nums.sort()
print('Ascending: ', nums)
nums.sort(reverse=True)
print('Descending: ', nums)
print('')

# Resetting numbers
nums = [3, 5, 1, 7, 2, 6]

# Some function
print('Minm valus: ', min(nums))
print('Maxm value: ', max(nums))
print('Summation: ', sum(nums))
print('')



# TUPLES - ()
# Tuples are similar to lists, the only difference being that tuples are immutable (u can't modify them), while lists are mutable (u can modify them)
tuple_1 = ('india', 'china', 'USA')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
print('')

# You can't modify a tuple (they are immutable). This following code will show error: -
"""
tuple_1[1] = 'pakistan'
print(tuple_1)
"""


# SETS {}
# Similar to lists, but the order or no. of times an item appears doesn't matter.
set_1 = {'cricket', 'football', 'badminton', 'volleyball', 'football', 'tennis'}
print('Outdoor games: ', set_1)

set_2 = {'billards', 'TT', 'badminton', 'volleyball', 'TT', 'squash'}
print('Indoor games: ', set_2)

print('')

# Sets are optimised for membership tests
print('cricket' in set_1)
print('cricket' in set_2)
print('')

# other functions
print('Intersection: ', set_1.intersection(set_2))
print('Union: ', set_1.union(set_2))
print('set1 - set2: ', set_1.difference(set_2))
print('set2 - set1: ', set_2.difference(set_1))