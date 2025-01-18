#Implement an Algorithm to determine if the string has all unqiue characters.

# 2018 This code uses additional data structure.
import re

user_input = input().strip()
unique = False

# save the characters of string in dictionary
dict_list={} 
i = 0

for chr in user_input:
    #Check if the char is already key in the dictionary
    if(dict_list.get(chr) == None ):
        #Add char as key in dictionary
        dict_list[chr] = i
        i +=1
        unique = True
    else:
        #Char is already present as key in dictionary
        unique = False
        break

if unique:
    print (user_input + " is unique string." )
else:
    print (user_input + " is not a unique string." )

# For loop n , O(n) complexity in worst case scenario, where n is the length of the string 

#2025 Jan
# Using Additional Data Structures - O(n) time and O(n) space
def has_unique_chars(s: str) -> bool:
    # Use a set to track characters
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# Example usage
print(has_unique_chars("abcdef"))  # True
print(has_unique_chars("hello"))   # False

# Without Using Additional Data Structures
# Time O(n log n ) , Space O(1)
def has_unique_chars_no_ds(s: str) -> bool:
    # Sort the string
    sorted_s = ''.join(sorted(s))
    # Check adjacent characters for duplicates
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    return True

# Example usage
print(has_unique_chars_no_ds("abcdef"))  # True
print(has_unique_chars_no_ds("hello"))   # False


