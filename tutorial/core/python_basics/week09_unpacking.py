#=== UNPACKING LSITS AND DICTIONARIES ===#

# converting all currencies into knuts
def total(galleons, sickles, knuts):
    return (galleons*17 + sickles)*29 + knuts

coins = [100, 50, 25]

# to pass this onto the function, one option is to use list indexing (NOT RECOMMENDED)
total_knuts_m1 = total(coins[0], coins[1], coins[2])
print(f"Total knuts (method 1): {total_knuts_m1}")

# the other recommed option is to use list unpacking
total_knuts_m2 = total(*coins)
print(f"Total knuts (method 2): {total_knuts_m2}")

# We can similary unpack a dictionary, giving it the affect of using keyword parameters
coins_dict = {"galleons": 100, "sickles": 50, "knuts": 25}
total_knuts_m3 = total(**coins_dict)        # use 2 asteriks (**) to unpack a dict
print(f"Total knuts (method 2): {total_knuts_m3}")


#=== ACCEPTING MULTIPLE ARGUMENTS: *args and **kwargs) ===#
"""
Functional parameters can be customised to accept varied number of positional (unnamed) and keyword arguments, which are stored in a tuple and dict respectively.
This can be done using a single asterik (*) for positional and double asterik (**) for keyword arguments, before the parameter name.
The parameters can be keyword anything, but the general convention is to use *args for positional and **kwargs for keyword parameters.

Note: All positional arguments MUST come before the keyword arguments
"""

def f(*args, **kwargs):
    print(f"Positional Arguments: {args}") 
    print(f"keyword Arguments: {kwargs}")

f("These", "are", "positional", "arguments", galleons=100, sickles=50, knuts=25)