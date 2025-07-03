'''STRINGS IN PYTHON (COMPLETE PLACEMENT-READY GUIDE)
🔹 1. What is a String?
A string is a sequence of characters (text), enclosed in either single (') or double (") quotes.

python
Copy code
s1 = 'Hello'
s2 = "World"
print(s1, s2)  # Output: Hello World
🔹 2. String Indexing and Slicing
Indexing allows you to access individual characters.

Indexing starts at 0.

python
Copy code
s = "Python"
print(s[0])    # 'P'
print(s[-1])   # 'n' (last character)
Slicing gets a part (substring) of the string.

python
Copy code
print(s[1:4])  # 'yth' (from index 1 to 3)
print(s[:3])   # 'Pyt' (start to index 2)
print(s[3:])   # 'hon' (index 3 to end)
🔹 3. String Immutability
Strings in Python are immutable, meaning you cannot change characters in a string directly.

python
Copy code
s = "Hello"
# s[0] = "J" ❌ This will give an error
s = "J" + s[1:]  # ✅ This creates a new string
print(s)         # "Jello"
🔹 4. Common String Methods
Method	Purpose
s.lower()	Converts to lowercase
s.upper()	Converts to uppercase
s.strip()	Removes leading/trailing spaces
s.replace(a, b)	Replaces a with b
s.split(" ")	Splits string into a list by space
' '.join(list)	Joins list into string
s.startswith("x")	Checks if string starts with x
s.endswith("x")	Checks if string ends with x

🔹 5. String Searching and Counting
python
Copy code
s = "banana"

print(s.find('a'))      # 1 (first index of 'a')
print(s.count('a'))     # 3
print(s.index('n'))     # 2 (like find but gives error if not found)
🔹 6. String Validation Methods
python
Copy code
s = "123"
print(s.isdigit())      # True
print(s.isalpha())      # False
print("hello".isalpha()) # True
Method	Checks if string is...
isdigit()	Only digits
isalpha()	Only letters
isalnum()	Letters and digits
isspace()	Only whitespace

🔹 7. Reversing a String
Using slicing:
python
Copy code
s = "Laxman"
print(s[::-1])  # "namxaL"
Using loop:
python
Copy code
rev = ""
for char in s:
    rev = char + rev
print(rev)
🔹 8. String Formatting
python
Copy code
name = "Laxman"
marks = 85

# Method 1: f-string (Python 3.6+)
print(f"{name} scored {marks} marks")

# Method 2: format()
print("{} scored {} marks".format(name, marks))
🔹 9. Useful Use-Cases in Data Analysis
Cleaning text columns using .strip(), .lower(), .replace()

Tokenizing using .split()

Checking formats using .startswith(), .isdigit()

Feature extraction: length of string, frequency of words

'''
'''
✅ Practice Questions (Try after reading above)
Write a program to reverse a string without using slicing.

Count the number of vowels in a string.

Remove all duplicate characters from a string.

Check if a given string is a palindrome.

Find the most frequently occurring character in a string.

Capitalize the first letter of each word in a string.

Convert "hello_world" into "Hello World".

'''
# Example code for practice questions
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize by lowercasing and removing spaces
    return s == s[::-1] 
def most_frequent_char(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return max(frequency, key=frequency.get)
def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())    
def convert_snake_to_title(s):
    return ' '.join(word.capitalize() for word in s.split('_')) 
# Example usage
if __name__ == "__main__":
    s = "hello world"
    print("Reversed String:", reverse_string(s))
    print("Number of Vowels:", count_vowels(s))
    print("String without Duplicates:", remove_duplicates(s))
    print("Is Palindrome:", is_palindrome   (s))
    print("Most Frequent Character:", most_frequent_char(s))        

    print("Capitalized String:", capitalize_first_letter(s))
    print("Converted Snake Case to Title Case:", convert_snake_to_title("hello_world")) 
    