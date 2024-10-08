# Exercise 1: Function Parameters
# Instructions:
# In this exercise, you will define functions with parameters.
# Write a function that accepts input parameters 
# and performs calculations or actions based on those parameters.
# Your task is to create a function that accepts 
# two numbers as parameters and prints their sum.

def add_numbers(a, b):
    # Your code here
    sum_result = a + b
    print(a,"+",b,"=", sum_result)
    pass

# Exercise 2: Return Values
# Instructions:
# Explore the concept of return values.
# Write functions that return results to the caller,
# allowing you to reuse computed values.
# Create a function that takes a list of numbers 
# as a parameter and returns the sum of those numbers.

def calculate_sum(numbers):
    # Your code here
    return(sum(numbers))
    pass


# Exercise 3: Function Scoping
# Instructions:
# Learn about the scoping of variables within functions.
# Work with global and local variables, and understand variable visibility.
# Create a function that uses a global variable and a local variable,
# and then print both variables to observe their scoping.

global_variable = "I am a global variable"

def demonstrate_scoping():
    # Define a local variable here
    local_variable = "I am a local variable"
    # Print both the global and local variables
    print(global_variable + "and" +local_variable)
    pass

# Exercise 4: Function Libraries
# Instructions:
# Create your own library of functions.
# Build a collection of functions that can be imported    
# and used in multiple programs.
# Rename/Convert the 'area.txt' file 
# to a Python module (area.py file) containing two functions - 
    # one that calculates the area of a rectangle 
    # and another that calculates the area of a circle.

# Import your custom function library
import area
def calculate_area(length, width, radius):
    # Example 1: 
    area_rectangle = area.area_rect(length, width) # Use the rectangle_area function from the Python module you created 
    print("Area of the rectangle:", area_rectangle)

    # Example 2: 
    area_circle = area.area_circ(radius) # Use the circle_area function from the Python module you created
    print("Area of the circle:", area_circle)

if __name__ == "__main__":
    add_numbers(2, 1)
    calculate_sum([1,2,3])
    demonstrate_scoping()
    calculate_area(5, 10, 4)