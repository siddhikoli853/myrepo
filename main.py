# day 3
# import pandas  # This is an example of external module
# import hashlib  # This is an example of built in module

# print("hi")

# Dont worry about how to use these modules just yet!
# pandas.read_csv("one.csv")
# m = hashlib.sha256()

#  day 4
# print("hi")

# day 5
# Single-Line Comments:
# Multi-Line Comments:
# Escape Sequence Characters
# More on Print statement
 
# day 6
# Variables and Data Types

#  day 10
# Taking User Input in Python

# a = int(input("square of your no. is "))
# print(a**2)

# day 11
# Strings In Python
# Quotation 
# Multiline string
# 
# a = "Strings"
# for char in a:
#     print(char)

# day12
# Strings Slicing and Operations on Strings in Python
# 1.Slicing from Start/End
# 2.Negative Indexing
# 3.Common String Operations
# name = "Siddhi"
# Length	len(name)	6
# Uppercase	name.upper()	SIDDHI
# Lowercase	name.lower()	siddhi
# Replace	name.replace("S", "K")	Kiddhi
# Check Prefix	name.startswith("S")	True

# day 13 
# String Methods in Python
# .upper() & .lower(): Converts the entire string to uppercase or lowercase.
# .title(): Capitalizes the first letter of every word.
# .capitalize(): Capitalizes only the very first letter of the string.
# .swapcase(): Flips lowercase to uppercase and vice-versa.
# .strip(): Removes all leading and trailing whitespace. (Very useful for CSV data!)
# .replace("old", "new"): Replaces all occurrences of a substring with another.
# .find("text"): Returns the index of the first occurrence of a word. Returns -1 if not found.
# .count("char"): Counts how many times a specific character or word appears.
# .isalpha(): Returns True if the string contains only letters (no numbers/spaces).
# .isdigit(): Returns True if the string contains only numbers.
# .islower() / .isupper(): Checks the casing of the string.
# .startswith("prefix") / .endswith("suffix"): Checks the beginning or end of a string.
# .split(","): Breaks a string into a list based on a separator.
# " ".join(list): Takes a list and combines it into one string with a space (or any character) between items.

# day14
# If Else Conditional Statements in Python
# if-else statements allow your program to make decisions. 
# They execute different blocks of code based on whether a condition is True or False.
# The elif Statement (Multiple Conditions)
# If you have more than two possibilities, use elif (short for "else if"). 
# Python checks these in order from top to bottom.
# Comparison Operators
# To create conditions, you'll use the common operators
# name = "Viddhi"

# if name.startswith("S"):
#     print("This name starts with S!")
# elif name.startswith("A"):
#     print("This name starts with A!")
# else:
#     print("This name starts with something else.")

# day16
# Match Case Statements in Python
# command = "save"

# match command:
#     case "open":
#         print("Opening file...")
#     case "save":
#         print("Saving file...")
#     case "exit":
#         print("Closing program...")
#     case _:
#         print("Unknown command")

# Matching Multiple Patterns

# day = "Saturday"
# match day:
#     case "Saturday" | "Sunday":
#         print("It's the weekend! 🎉")
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print("It's a workday. 💻")
# You can use the pipe symbol (|) to match multiple values in a single case,
# which is much cleaner than using or in an if statement.

# Match Case with Conditions (Guards)

# age = 21

# match age:
#     case n if n < 13:
#         print("Child")
#     case n if n < 20:
#         print("Teenager")
#     case _:
#         print("Adult")
# You can add an if statement to a case for even more control. 
# This is called a Guard.
 
# day17
# For Loops in Python

# names = ["siddhi", "nisha", "serena"]
# for name in names:
#     print(name)
# for i in range(5):
#     print(f"Iteration number: {i}")

# numbers = [1,2,3,4,5,6,7,8,9]
# for number in numbers:
#     if number == 3:
#         continue
#     if number == 8:
#         break
#     print(number)

# raw_names = [" siddhi", "yash ", "  nisha"]

# for name in raw_names:
#     clean_name = name.strip().capitalize()
#     print(f"Hello, {clean_name}!")

# Day18
# Python While Loops

# Python has two primitive loop commands:

# while loops
# for loops
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
# i = 1
# while i < 8:
#     print(i)
#     if i == 5:
#         break
#     i+=1
# i = 1
# while i < 8:
#         i+=1
#         if i == 5:
#             continue
#         print(i)

# day19
# break,pass and continue in Python
# In Python, break, continue, and pass 
# are used to control the flow of loops and handle empty code blocks.
# for i in range(1, 10):
#     if i == 5:
#         break  # Stops the loop when i is 5
#      print(i)
# for i in range(1, 6):
#     if i == 3:
#         continue  # Skips printing 3
#     print(i)
# if True:
#     pass  # I will add logic here later!

# print("Code runs because pass filled the empty block")
# break	Stops the loop completely.	You found what you were looking for.
# continue	Skips the rest of the current turn.	You want to ignore one specific item.
# pass	Does nothing at all.	Placeholder to prevent errors

# day20
# Python Functions
# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.
# In Python, a function is defined using the def keyword, followed by a function name and parentheses
# def my_function():
#   print("Hello from a function")

# my_function()
# my_function()
# my_function()

# def fahrenheit_to_celsius(fahrenheit ):
#     return (fahrenheit -32)*5/9

# print(fahrenheit_to_celsius(50))
# print(fahrenheit_to_celsius(89))

# day21
# Python Function Arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
# def my_function(name): # name is a parameter
#   print("Hello", name)

# my_function("siddhi") # "siddhi" is an argument

# If your function expects 2 arguments, you must call it with exactly 2 arguments.
# If you try to call the function with the wrong number of arguments, you will get an error:

# Default Parameter Values

# def my_function(x="siddhi"):
#     print ("hello" ,x)

# my_function()
# my_function("yash")

# Keyword Arguments
# You can send arguments with the key = value syntax.

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(animal = "dog", name = "Buddy")


# day29
# Docstring
# In Python, a Docstring (short for documentation string) is a special type of string used to explain what a specific module, function, class, or method does. Unlike regular comments (#), docstrings are actually stored as part of the code's metadata, making them accessible while the program is running.

# def greet(name):
#     """This function greets the person passed in as a parameter."""
#     print(f"Hello, {name}!")

# greet("siddhi")    

# How to Access Docstrings
# print(greet.__doc__)
# help(greet)

# day 30
# Recursion in Python
# Recursion is when a function calls itself.

# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite 
# easy to slip into writing a function which never terminates, or one that 
# uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and 
# mathematically-elegant approach to programming.

# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(5)

# Base Case and Recursive Case
# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument

# def factorial(n):
#   # Base case
#   if n == 0 or n == 1:
#     return 1
#   # Recursive case
#   else:
#     return n * factorial(n - 1)

# print(factorial(8))

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# day36,37,38
# Exception Handling in Python:
#  link = https://www.w3schools.com/python/python_try_except.asp



