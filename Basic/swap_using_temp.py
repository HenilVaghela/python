# Program to swap two numbers using a temporary variable

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

temp = x
x = y
y = temp

print(f"After swap: x = {x}, y = {y}")
