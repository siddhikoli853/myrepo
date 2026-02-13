# day 22
# Python Lists

# Lists are created using square brackets:
# Lists are used to store multiple items in a single variable
# Lists are one of 4 built-in data types in Python used to store collections
# of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# thislist = ["apple", "banana", "cherry"]
# print(thislist) 

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# A list with strings, integers and boolean values:

# list1 = ["abc", 34, True, 40, "male"]
# print(type(list1))

# Python - Access List Items
# link = "https://www.w3schools.com/python/python_lists_access.asp"

# List Methods
# Method - Description
# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Add the elements of a list (or any iterable), to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop()	- Removes the element at the specified position
# remove()	- Removes the item with the specified value
# reverse()	- Reverses the order of the list
# sort() - Sorts the list

# link = https://www.w3schools.com/python/python_lists_methods.asp

# day24
# Python Tuples
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# mytuple = ("apple", "banana", "cherry")
# print(mytuple)
 
# day25
# Python - Tuple Methods
# count() - Returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position of where it was found
 
# day 28
# f-string
# txt = f"The price is {20 * 59} dollars"
# print(txt)

# price = 59
# print(f"The price is {price:.2f} dollars")
 
# day31 Set in Python
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# Unordered: Items do not have a defined order, so you cannot access them by index (like my_set[0]).
# Unique Items: Sets automatically remove any duplicate values you try to add.
# Unchangeable Items: You cannot change the items once added, but you can add new items or remove existing ones.
# Important Note: To create an empty set, you must use set(). Using {} will create an empty dictionary.


# Common Set Methods
# .add(x)	Adds one item to the set.	my_set.add(".csv")
# .update(list)	Adds multiple items from another collection.	my_set.update([1, 2, 3])
# .remove(x)	Removes an item. Raises an error if not found.	my_set.remove("Siddhi")
# .discard(x)	Removes an item. Does not error if missing.	my_set.discard("OldData")
# .pop()	Removes a random item (since sets are unordered).	val = my_set.pop()

# Mathematical Set Operations
# This is where sets truly shine. Python allows you to perform operations similar to Venn diagrams.

# Union (|): Combines all items from both sets.
# Intersection (&): Keeps only items present in both sets.
# Difference (-): Keeps items in the first set that are not in the second.
# Symmetric Difference (^): Keeps items that are in either set, but not both.

# Python Dictionaries

# Ordered: As of Python 3.7, dictionaries maintain the order in which items are inserted.
# Changeable: You can change, add, or remove items after the dictionary is created.
# Unique Keys: You cannot have two items with the same key. If you add a duplicate key, the old value will be overwritten.
# Key Types: Keys must be immutable (strings, numbers, or tuples), while values can be anything (lists, other dictionaries, etc.).

# Creating a dictionary for your project
# user_info = {
#     "name": "Siddhi",
#     "role": "Developer",
#     "repo": "localrepo"
# }

# # Accessing a value
# print(user_info["name"])  # Output: Siddhi

# # Adding or Updating
# user_info["language"] = "Python"  # Adds a new pair
# user_info["role"] = "Lead Dev"

# Essential Dictionary Methods
# .get(key)	Returns the value of a key. Doesn't error if key is missing.	user_info.get("age")
# .keys()	Returns a list of all the keys.	user_info.keys()
# .values()	Returns a list of all the values.	user_info.values()
# .items()	Returns a list of tuples (key, value pairs).	user_info.items()
# .update({k:v})	Updates the dictionary with the specified key-value pairs.	user_info.update({"status": "active"})
# .pop(key)	Removes the item with the specified key name.	user_info.pop("role")

# 4. Looping Through Dictionaries
# Because dictionaries have both keys and values, you have three ways to loop:

# Python
# # Loop through keys
# for key in user_info:
#     print(key)

# # Loop through values
# for val in user_info.values():
#     print(val)

# # Loop through both (Most common)
# for key, value in user_info.items():

# Example: Using a dictionary to represent a row in your one.csv
# row_data = {
#     "filename": "index.html",
#     "status": "conflict",
#     "line_count": 18
# }

# if row_data["status"] == "conflict":
#     print(f"Warning: {row_data['filename']} needs a merge fix!")

# day35

# for Loop with else in Python 

# The else block executes only if the loop finishes all its iterations naturally (i.e., it reaches 
# the end of the sequence). If the loop is stopped prematurely by a break 
# statement, the else block is skipped entirely.

# files = ["index.html", "main.py", "one.csv", "style.css"]
# search_file = "readme.md"

# for file in files:
#     if file == search_file:
#         print(f"Found it: {file}")
#         break
# else:
#     # This only runs if the loop searched every file and found nothing
#     print(f"Error: {search_file} is not in the repository.")





