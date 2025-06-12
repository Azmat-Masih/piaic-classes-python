'''
Handling The exception with try-except

To prevent the program from crashing, we can use try-except to handle the exception.
'''

def divide(a : int, b : int):
    if b == 0:
        raise ValueError("Division by zero is not allowed !")
    return a / b

try:
    result = divide(10,5) # throw an error
    print(result) # will not print
except ValueError as e:
    print(f"Error:  {e}")
    
print("Program Continues ")