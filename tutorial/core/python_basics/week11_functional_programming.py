"""
PROGRAMMING PARADIGMS
    There are many programming paradigms. Some of them are:
        Procedural Programming 
            - give computer a set instructions, called procedures to follow
            - eg. C, Pascal, Unix Shells
        Object-Oriented Programming
            - organize code as collection of objects
            - eg. Java, Smalltalk
        Declarative Programming
            - tell the computer what you want, not how to do it
            - eg. SQL
        Functional Programming
            - decomposes the problem into set of functions, which don't change the state of the program
            - eg. Haskell, ML Family (standard ML, OCaml, and other variants)

FUNCTIONAL PROGRAMMING
    The core idea of functional programming is to break the problem into pure functions. Pure functions are those functions which neither change the state of the program nor produce any side effects (like printing something on the terminal [using print(...)] or pausing the execution of the program with sys.sleep()

    The functions here do not depend on external variables, and for a given input, the output  


ITERATORS

"""



#=== GENERATORS ===#
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

"""
This above function returns a list of rows of sheeps. If we pass in 1M, the function will return a list of 1M items, with each item containing one more sheep then the previous item.
This will create a massive list, for which enough memory is not present, thus leading the program to crash with a MemoryError.
"""
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

"""
The above problem can be solved using yield
"""
def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()