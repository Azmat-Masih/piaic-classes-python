'''
Throwing Custom Exceptions :

Python also allows you to define custom 
exceptions by creating a new class that 
inherits from Exception.
'''

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"

try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!

     

'''
Summary

-Use raise to throw an exception inside a function.

-Use try-except to handle exceptions and prevent crashes.

-Create custom exceptions by inheriting from Exception.
'''