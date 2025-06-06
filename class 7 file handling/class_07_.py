# File Handling


'''
Modes: 

r = read (by default)
w = write (opens the file and write, if the file dosen't exit it will create, and overwrite)
a = append (append, if the file dosen't exit it will create,)
x = exclusive creation (if file dosen't exit)
b = binary mode, (rb, wb)
+ = update mode (can be combined with other modes) ('r+','w+') to allow both reading and writing.

'''

# Practice

# example 01 (write the file)
file = open("practice.txt", "w")
file.write("this is the txt\n")
file.close() # old method / now we use with block to auto close the file

# example 02 (reading the file)
file = open("practice.txt","r") 
file.close()

# example 03 (append the file)
data_ : str = "this is new data \n"
file = open("practice.txt","a")
file.write(data_)

# example 04 (writing lines (list) )
lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
file = open("practice.txt", "a") # run with mode w, and see the result
file.writelines(lines) # write lines = (list)
file.close()


# example 05 (reading the file)
file = open("practice.txt","r")
content = file.read()
print(content) 



'''

In Python, a file pointer (also called a file cursor or file position indicator) is 
an internal marker that keeps track of the current position in a file where the next 
read or write operation will occur. When you open a file, the file pointer is initialized 
to a specific position (usually 0, the beginning of the file), and it moves automatically
as you read from or write to the file.


Key Concepts:

Starting Position:

r = (read mode): Pointer starts at 0 (beginning of the file).
a = (append mode): Pointer starts at the end of the file.
w = (write mode): The file is truncated (erased), and the pointer starts at 0.


How It Moves:
When you read/write data, the pointer moves forward by the number of 
bytes/characters processed.

Example: Reading 10 characters moves the pointer 10 positions forward.
Manual Control:
Use seek(offset) to move the pointer to a specific byte position.
Use tell() to check the current pointer position.
'''

# example 06
# seek() to move the pointer to a specific byte position
# tell() to check the current pointer position

file.seek(0) #moves the pointer to 0
print("position of the pointer", file.tell()) #tells the position of the pointer

# example 07
# readline() = read  all the lines into a list
'''
readline()
Reads a single line from the file.

You can call it repeatedly to read lines one by one.

Useful when processing a file line-by-line, especially for large files.
'''
line = file.readline()
print(line)


# example 09
# readlines() = read all the lines at once in list form
'''
readlines()

Reads all lines at once and returns them as a list of strings.
Each list item is one line from the file.
Not memory-efficient for very large files.'''
line = file.readlines()
for line in lines:
    print(line)
    
file.close()
    

# example 10
# strip() = removes leading/trailing white space
file = open("practice.txt", "r")
for line in file:
    print(line.strip()) #removes leading/trailing white space
    
file.close()


# example 11
'''
Use with for automatic cleanup.
Handle exceptions to avoid crashes.
'''
try:
    with open("unique.txt", "x") as file:
        file.write('Created exclusively!')
except FileExistsError:
    print("File already exists.")
    


# example 12
# with Statement
'''
The best practice for file handling is to use the with statement. 
This ensures that the file is automatically closed, even if errors occur.
'''

with open("practice.txt","r") as file:
    content = file.read()
    print(content)
# now file automatically closed  

# file.tell() "throws error now because the file is closed"



# example 13
"create and write to a file"
with open("demo.txt","w") as file:
    file.write("this is the demo content. \n")
    file.write("this is Bill Gates. \n")
    
"read and print content"
with open("demo.txt","r") as file:
    content = file.read()
    print(content)
    
"append a new line"
with open("demo.txt","a") as file:
    line = "this is satoshi nakamoto.\n"
    file.write(line)
    
"read lines using seek"
with open("demo.txt","r+") as file:
    file.seek(0)
    print("this is the first line => ", file.readline())
    


# example 14
"prompt: generate a comprehensive example of file handling using all the functions"

# Step 1: Create and write to a file
file = open("sample.txt", "w")  # Open file in write mode
file.write("Line 1: Hello, world!\n")
file.write("Line 2: Welcome to file handling in Python.\n")
file.writelines([
    "Line 3: This is written using writelines().\n",
    "Line 4: Another line added using writelines().\n"
])
file.close()  # Always close the file when done

# Step 2: Read entire content using read()
file = open("sample.txt", "r")
print("🔹 Full content using read():")
content = file.read()
print(content)
file.close()

# Step 3: Read line-by-line using readline()
file = open("sample.txt", "r")
print("🔹 Reading line-by-line using readline():")
print(file.readline(), end='')  # Line 1
print(file.readline(), end='')  # Line 2
file.close()

# Step 4: Read all lines into a list using readlines()
file = open("sample.txt", "r")
print("🔹 All lines as list using readlines():")
lines = file.readlines()
print(lines)
file.close()

# Step 5: Demonstrate tell() and seek()
file = open("sample.txt", "r")
print("🔹 Current file pointer using tell():", file.tell())  # Should be 0
print("Reading first 10 characters:", file.read(10))
print("🔹 File pointer after reading 10 characters:", file.tell())  # Should be 10

file.seek(0)  # Move pointer back to start
print("🔹 After seek(0), reading again:")
print(file.readline(), end='')  # Line 1
file.close()

# Step 6: Using with-statement (auto handles close)
print("🔹 Using with-statement:")
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())  # Remove newline for clean output
