"""Solving using no other data structure. In this bitwise operators are used to check a bit if it is present and 
if the checked bit is accessed again then the string doesn't have unique letters"""

def all_unique_nods(s):
    s = s.lower()
    checker = 0 #taking 0 

    for ch in s:
        val = ord (ch) - ord ('a') #subtracting the ascii values
        if (checker & (1 << val)) > 0: #checking if the bit is already 1
             return "Not Unique"

        checker = checker|(1 << val)   #if not already 1, then set to 1
    return "Unique"

def main():
    s = input("Enter a string: ")
    print("Result using no other data structure: " + all_unique_nods(s))

if __name__ == "__main__":
    main()
