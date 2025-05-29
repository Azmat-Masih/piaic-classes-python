'''
Control Flows in Python (if, elif, else, with, for, while, try, excepts)

If, elif, else (statements)

'''

user_name : str = input("write your name: ")
user_password : str = input("write your password: ")
  # _otp_ : int = int(input("write your otp: "))

if(user_name == "admin" and user_password == "admin123"):
  _otp_ : int = int(input("write your otp: "))
  if(_otp_ == 1234):
    print("welcome admin")
  else:
    print("wrong otp")
else:
  print("invalid user: ")
  
  
  
'''
# prompt: Write a program that takes an integer from the user and prints whether it is even or odd.

# Get input from the user
'''

try:
    num = int(input("Enter an integer: "))

    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")
    
    
    
num_ : int = int(input("write a number: "))

if(num_ >= 80 and num_ <= 100):
  print("A+")
elif(num_ >= 70 and num_ <= 79):
  print("A")
elif(num_ >= 60 and num_ <= 69):
  print("B")
elif(num_ >= 50 and num_ <= 59):
  print("C")
elif(num_ >= 40 and num_ <= 49):
  print("D")
elif(num_ >= 33 and num_ <= 39):
  print("E")
else:
  print("Fail")
  
  
  
  
    
'''
# prompt: generate the above grading system. but use match case, instead of if else.
'''

num_ : int = int(input("write a number: "))

match num_:
  case num_ if 80 <= num_ <= 100:
    print("A+")
  case num_ if 70 <= num_ <= 79:
    print("A")
  case num_ if 60 <= num_ <= 69:
    print("B")
  case num_ if 50 <= num_ <= 59:
    print("C")
  case num_ if 40 <= num_ <= 49:
    print("D")
  case num_ if 33 <= num_ <= 39:
    print("E")
  case _:
    print("Fail")
    
    
    
    
'''   
# prompt: Use match-case to print the word for a digit between 0–5. For example, input 3 → output: "Three".
'''


digit = int(input("Enter a digit between 0 and 5: "))

match digit:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid input. Please enter a digit between 0 and 5.")
        





'''
For loops (in python, used when the set of data is limited. )
'''

name : str = "VELO"

for i in name:
  print(i)
  



 
fruit_list : list = ["apple", "banana", "grapes", "orange", "Tim Cook"]

for i in fruit_list:
  print(i)



num_ : int = int(input("Write num here: "))

for i in range(1,11):
  print(f"{num_} x {i} = {i * num_}")
  


'''
# prompt: Print numbers from 1 to 50. For multiples of 3, print "Fizz", for 5 print "Buzz", for both print "FizzBuzz".
'''

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
        
'''
# prompt: Ask the user for a number N and use a for loop to calculate the sum from 1 to N.
'''

n = int(input("Enter a number: "))

sum_of_numbers = 0
for i in range(1, n + 1):
  sum_of_numbers += i

print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")
