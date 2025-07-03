'''Part 1: Introduction to Functions in Python
✅ What is a Function?
A function is a reusable block of code that performs a specific task.

python
Copy code
def greet():
    print("Hello, Laxman!")
✅ Why Use Functions?
Avoid repeating code (DRY Principle – Don't Repeat Yourself)

Improve readability and organization

Helps with debugging and testing

📘 Part 2: Defining and Calling a Function
✅ Syntax:
python
Copy code
def function_name():
    # block of code
✅ Example:
python
Copy code
def welcome():
    print("Welcome to Python Functions!")

welcome()  # Calling the function
📘 Part 3: Function with Parameters
✅ Example:
python
Copy code
def greet(name):
    print("Hello", name)

greet("Laxman")
greet("Shyam")
name is a parameter

"Laxman" is an argument

📘 Part 4: Function with Return Value
✅ Example:
python
Copy code
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
return sends back the result to the caller

📘 Part 5: Default Parameters
python
Copy code
def greet(name="Friend"):
    print("Hello", name)

greet()          # Output: Hello Friend
greet("Laxman")  # Output: Hello Laxman
📘 Part 6: Keyword vs Positional Arguments
✅ Positional:
python
Copy code
def info(name, age):
    print(name, age)

info("Laxman", 21)
✅ Keyword:
python
Copy code
info(age=21, name="Laxman")
📘 Part 7: *args and **kwargs (Advanced but Useful)
✅ *args – for variable number of positional arguments
python
Copy code
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))  # Output: 6
✅ **kwargs – for variable number of keyword arguments
python
Copy code
def print_info(**person):
    for key, value in person.items():
        print(key, ":", value)

print_info(name="Laxman", age=21)
🧠 Interview Tip:
Functions with parameters and return values are basic building blocks in every Python program and expected in any coding question.
'''
'''✅ Practice Questions (You’ll Solve These After Learning)
Write a function to find the factorial of a number.

Create a function that checks if a string is a palindrome.

Write a function to return the maximum of 3 numbers.

Create a function to reverse a list.

Write a function that accepts a list and returns the sum of even numbers.
'''

# Example code for practice questions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
def is_palindrome(s):
    return s == s[::-1] 
def max_of_three(a, b, c):
    return max(a, b, c)
def reverse_list(lst):
    return lst[::-1]  # Using slicing to reverse the list
def sum_of_evens(lst):
    return sum(x for x in lst if x % 2 == 0)
# Example usage of practice functions
print(factorial(5))  # Output: 120

print(is_palindrome("radar"))  # Output: True
print(max_of_three(10, 20, 15))  # Output: 20
print(reverse_list([1, 2, 3, 4, 5]))
# Output: [5, 4, 3, 2, 1]
print(sum_of_evens([1, 2, 3, 4, 5, 6]))  # Output: 12
