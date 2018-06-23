#Implement an Algorithm to determine if the string has all unqiue characters.

#This code uses additional data structure.
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
