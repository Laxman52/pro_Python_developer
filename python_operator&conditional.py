'''Stage 2 – Operators, Conditional Statements, and Loops
This is CRITICAL — helps in data cleaning, ETL scripting, and logic building for small data tasks.

📘 Topic 4: Operators in Python
➤ Arithmetic Operators:
python
Copy code
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000
➤ Comparison Operators:
python
Copy code
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a <= b)  # False
➤ Logical Operators:
python
Copy code
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
📘 Topic 5: If-Else Conditions
python
Copy code
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for placement.")
else:
    print("Not eligible yet.")
➤ Elif Example:
python
Copy code
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

'''
#🏋️‍♂️ Practice Questions:
#Write a program to check if a number is even or odd. Take a number as input and print if it is: Positive ,Negative Or Zero
# Program to check if a number is even or odd, and if it is positive, negative, or zero

num = int(input("Enter a number: "))


if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")+
'''

📘 Topic 6: Loops
➤ For Loop:
python
Copy code
for i in range(1, 6):
    print(i)
➤ While Loop:
python
Copy code
i = 1
while i <= 5:
    print(i)
    i += 1
➤ Loop with break and continue:
python
Copy code
for i in range(10):
    if i == 5:
        break  # exits loop
    print(i)

for i in range(5):
    if i == 2:
        continue  # skips this iteration
    print(i)
✅ Importance for Interviews:
Loop + condition is frequently used in coding rounds.

Used in data filtering and basic EDA steps.

🚀 Mini Project Task:
'''
# Write a program to print FizzBuzz from 1 to n:If divisible by 3 → print "Fizz" If divisible by 5 → print "Buzz" If both → print "FizzBuzz" Else → print the number

#python
# Sample output
#1

#2
#Fizz
#4
#Buzz
#Fizz

# FizzBuzz program from 1 to n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)