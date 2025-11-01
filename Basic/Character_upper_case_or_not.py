# Program to check if a character is uppercase, lowercase, or not an English letter

ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only a single character.")
elif 'A' <= ch <= 'Z':
    print("Upper case")
elif 'a' <= ch <= 'z':
    print("Lower case")
else:
    print("Not an English letter")
