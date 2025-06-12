'''
What is NoReturn?

NoReturn is a special type hint from Python's typing module. It is used to indicate that a
function will not return normally. This means the function either:

-Always raises an exception,
-Enters an infinite loop,
-Or otherwise never reaches the end of the function body to return a value.
'''

'''
When Would You Use NoReturn?

-Functions that Always Raise Exceptions: For example, a function that immediately raises 
an error can be annotated with NoReturn to signal that it doesn't produce a return value.

-Infinite Loops: A function that runs forever (or until the program is terminated) is a 
candidate for NoReturn.

'''


from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the program.")

# When you call terminate_program, it never returns normally:
try:
    terminate_program()
except SystemExit as e:
    print(f"Program terminated: {e}")
    
    
'''
Why Use NoReturn?

-Improved Readability: It makes your intent clear to anyone reading your code.

-Better Static Analysis: Tools like mypy can use these annotations to detect issues 
in your code, ensuring that functions marked with NoReturn truly do not return a

'''



'''
Alternative: Using None Instead of NoReturn

If your function does not return any meaningful value but does not necessarily 
terminate the program (e.g., it performs logging, prints messages, etc.), you can 
use None as the return type instead of NoReturn.


✔ Use -> None when the function completes execution but does not return a value.

❌ Do NOT use -> None if the function always raises an exception or runs indefinitely.

'''
def log_error(message: str) -> None:
    """Logs an error message but does not terminate the program."""
    print(f"Error: {message}")

log_error("Something went wrong!")



'''
Alternative: Omitting the Return Type Hint

Python does not require type hints, so if you are not using static type checking tools 
like mypy, you can simply omit the return type hint.
'''
def terminate_program():
    """Terminates the program by raising an exception."""
    raise SystemExit("Program is terminating.")

terminate_program()




'''
When Should You Stick to NoReturn?
If you are using type checking tools like mypy, NoReturn is still the best choice for 
functions that:

-Always raise an exception

-Never return (e.g., an infinite loop)

-Terminate the program (sys.exit())

But if you are not using static type checking, omitting the type hint or using None may 
be enough.
'''