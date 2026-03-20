# LOOPS

# FOR LOOP
print('')

nums = [1, 2, 3, 4, 5, 6]

'''
for num in nums:    # We r looping through each value of a list and during each iteration, the value of that element is stored in nums. 
    print(num)
    print('')
'''

for num in nums:
    if num==2:      # Skipping the rest of the loop is num == 2, thus, not printing 2
        continue 
    if num==5:
        print('Found 5! Exiting the loop')
        break       # Exiting loop when num==4, thus printing nos only till 3
    print(num)  

print('')

# Nested loops. It's pretty easy

# Range
for i in range(5):      # prints nos from 0 upto (not inclusive) 5 
    print(i)
print('')


for i in range(13, 17):    # starts from 2
    print(i)
print('')


# WHILE LOOP
w = 0
while w<5:      # basic while loop
    print(w)
    w += 1


# Infinte while loop untill break is encountered
x = 0
while 1:
    if x==4:
        break
    print(x)
    x += 1