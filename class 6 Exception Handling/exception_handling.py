'''
Exception Handling with try, except, else, and finally 






try block = The try block is used to test a block of code for errors. If an error occurs within the try block, 
            the program will immediately jump to the except block (if provided).

except block = The except block is used to handle specific errors that occur in the try block. You can specify 
               the type of error to catch, or use a generic except to catch all errors.

Else block = The else block is executed if no errors occur in the try block. It is optional and is used for code 
             that should only run when the try block is successful

finally block = The finally block is executed regardless of whether an error occurred or not. It is often used for 
                cleanup operations, such as closing files or releasing resources.

'''


# Example 01 "try block"
try:
    result = 10/0
except:
    print("an error occurred ! ")


# Example 02 "except block"
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero ! ")
except Exception as e:
    print(f"an unexpected error occurred {e}")


# Example 03 "else block"
try:
    result = 10/2
except Exception as e:
    print(f"an error accurred {e} ! ")

else:
    print("this will always excute ==> ", result)


# Example 04 "finally block"
try:
    result = 10 / 2

except ZeroDivisionError:
    print("can not divide by zero ")
    
else:
    print("this is the else block ==> ", result)
    
finally:
    print("This will always excute ! finally block ")
    

# Example 05 "All together"
def allErrorHandlingTogether(a:int, b: int):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Cann't divide by Zero !")
    else:
        print("Result ", result)
    finally:
        print("this will excute no matter whats the error is !")

# allErrorHandlingTogether(10,0) #Out put zero division error
# allErrorHandlingTogether(6,3) # it will excute without any error


'''
Key Points : 

try block: used to test a block of code for error
except block: used to handle specific or generic errors
else block: excutes when no errors occur in the try block
finally block: Excute regardless of whether an error occured
'''


#  prompt: generate a learning code on error handling covering all the expects

# ----------------------------------------
# 1. Basic try/except block
# ----------------------------------------
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

# ----------------------------------------
# 2. Catching all exceptions
# ----------------------------------------
try:
    value = [1, 2, 3]
    print(value[5])  # IndexError
except Exception as e:
    print(f"General error caught: {e}")

# ----------------------------------------
# 3. Try/except/else
# ----------------------------------------
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")
else:
    print(f"You're {age} years old.")

# ----------------------------------------
# 4. Try/except/finally
# ----------------------------------------
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    print("This block always runs.")
    if 'file' in locals() and not file.closed:
        file.close()

# ----------------------------------------
# 5. Manually raising an exception
# ----------------------------------------
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Manual Error: Division by zero is not allowed.")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print(f"Custom raise caught: {e}")

# ----------------------------------------
# 6. Custom Exception class
# ----------------------------------------
class NegativeNumberError(Exception):
    """Raised when a negative number is passed."""
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return True

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Custom Exception caught: {e}")

# ----------------------------------------
# 7. Multiple exceptions in one line
# ----------------------------------------
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
except (ValueError, TypeError) as e:
    print(f"Multiple exception types caught: {e}")

# ----------------------------------------
# 8. Nested try blocks
# ----------------------------------------
try:
    try:
        val = int("abc")  # ValueError
    except ValueError:
        print("Inner block: ValueError caught.")
    print(10 / 0)  # ZeroDivisionError
except ZeroDivisionError:
    print("Outer block: ZeroDivisionError caught.")



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