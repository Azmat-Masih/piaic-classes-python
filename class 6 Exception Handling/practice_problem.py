'''
Practice Problem:

Write a Python program that asks the user for two numbers and divides them. 
Use exception handling to catch any errors that might occur (e.g., division 
by zero or invalid input).
'''

try:
    num1 :int = float(input("enter the number: "))
    num2 :int = float(input("enter the second number: "))
    result = num1 / num2

except ValueError:
    print("Error: Invalid input, please enter the number. ")
except ZeroDivisionError:
    print("Error: cann't divide by zero")
else:
    print("result", result)
finally:
    print("thank you for using the program ! ")
    
    

'''
How a Function Throws an Exception in Python?

In Python, a function can throw an exception using the raise keyword. 
This is used to indicate that an error has occurred, and it interrupts 
the normal flow of the program.

When an exception is raised:
Python immediately stops executing the function.
The error message is displayed unless the exception is handled using try-except.
'''


def deivide(a : int, b :int):
    if b==0:
        raise ValueError("Division by zero is not allowed") # 
    return a/b

# print(deivide(19,2)) # output : without any error  
print(deivide(5,0)) # Raises : ValueError : Division by zero is not allowed !


