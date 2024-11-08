# Caitlyn Ganskow
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: None


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def int_or_float(number):
    """takes in a string, checks if it is integer or float, then converts them"""
    if "." in number:
        return int(float(number))
    elif number.isnumeric():
        return float(number)
    else:
        return False

num1 = "56"
num2 = "7.8"
num3 = "k"

print(int_or_float(num1))
print(int_or_float(num2))
print(int_or_float(num3))

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list



def point_slope(m, b, lx, ux):
    """collects 4 numbers then uses point-slope formula to return values of y within range given"""
    y_values = []
    if "." in lx or "." in ux:
        return False
    elif int(lx) > int(ux):
        return False
    elif m.isalpha() or b.isalpha() or lx.isalpha() or ux.isalpha():
        return False
    else:
        for x in range(int(lx), int(ux)):
            y = float(m)*x + float(b)
            y_values.append(y)
        return y_values

while True:
    user_input = input("please input a m, b, lower x, upper x: type 'exit' to quit")
    if user_input.lower() == 'exit':
        break
    else:
        numbers = user_input.split(", ")
        um = numbers[0]
        ub = numbers[1]
        ulx = numbers[2]
        uux = numbers[3]
        print(point_slope(um, ub, ulx, uux))


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_formula(a, b, c):
    root = square_root(a, b, c)
    if root == "null":
        return "Cannot find"
    else:
        return ((-b+root)/(2*a)), ((-b-root)/(2*a))

def square_root(a, b, c):
    under_root = b**2 - 4*a*c
    if str(under_root).startswith("-"):
        return "null"
    else:
        return (under_root)**.5

while True:
    user_input = input("please input a number for a, b, c or type 'exit' to quit")
    if user_input.lower() == 'exit':
        break
    else:
        numbers = user_input.split(", ")
        ua = int(numbers[0])
        ub = int(numbers[1])
        uc = int(numbers[2])
    print(quadratic_formula(ua, ub, uc))