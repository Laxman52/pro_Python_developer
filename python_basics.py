# Stage 1 – Python Basics for Data Analysis
''' Topic 1: Variables & Data Types
➤ What is a variable?
A variable is just a name that refers to a value.

python
Copy code
name = "Laxman"
age = 21
marks = 85.5
is_placed = False
➤ Python Data Types:
Type	Example
int	10, -3, 0
float	3.14, -2.7
str	'hello', "abc"
bool	True, False

✅ You don’t need to declare types — Python is dynamically typed.

🧪 Practice:
python
Copy code
# Declare your own details
my_name = "Laxman"
my_age = 21
my_cgpa = 8.5
placed = False

print(my_name)
print(my_age)
print(my_cgpa)
print(placed)
📘 Topic 2: Type Casting
Convert between types using int(), float(), str(), bool():

python
Copy code
a = "25"
print(int(a) + 5)   # 30

b = 3.99
print(int(b))       # 3

c = 1
print(bool(c))      # True
📘 Topic 3: Input & Output
python
Copy code
name = input("Enter your name: ")
print("Welcome", name)
Everything you take via input() is a string by default:


age = int(input("Enter your age: "))
print(age + 1)'''
#Exercise: Basic Input and Output

#Write a program that:

#Takes your name, age, and cgpa from user input

#Increases age by 1

#Prints in a sentence format

name=input("Enter your name: ")
age=input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")
age=int(age)+1
print(f"Next year, you will be {age} years old.")

print("Thank you for using the program!")