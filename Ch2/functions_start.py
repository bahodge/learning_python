#
# Example file for working with functions
#

# define a basic function
def func1():
    print("i am a function")
    return "hello"


# function that takes arguments

def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value

def myCube(x):
  print(x*x*x)

# function with default value for an argument

def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

def multi_mult(num, *args):
    result = num
    for x in args:
        result = num * x
    return result


func1()
print(func1())
print(func2("Ben", "Rocks!!!"))
print(myCube(3))
print(power(2))
print(power(2, 3))
print(multi_add(1, 2, 3, 4, 5))
print(multi_mult(10, 3, 5, 6)) #tis strange!!!