# 
# Example file for variables
#


# Declare a variable and initialize it

f = 0
print(f)
# # re-declaring the variable works

f = "abc"
print(f)
# # ERROR: variables of different types cannot be combined

# f = 100 - "hello" # type error

f = str(123) + "hello"
print(f)
# Global vs. local variables in functions

def someFunction():
    global f
    f = "def"
    # local method scope


someFunction()
print(f)


del f #deletes f definition
print(f) #undefined error