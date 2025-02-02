# CALCULATOR

import math

print("Welcome to my Python Calcultaor!")
print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. SQUARE A NUMBER")
print("Write your option here:")

operation = input()

if operation == "1": # PERFORMS ADDITION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is "+ str(int(num1) + int(num2)))

elif operation == "2": # PERFORMS SUBTRACTION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is "+ str(int(num1) - int(num2)))

elif operation == "3": # PERFORMS MULTIPLICATION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is "+ str(int(num1) * int(num2)))

elif operation == "4": # PERFORMS DIVISION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is "+ str(int(num1) / int(num2)))

elif operation == "5": # PERFORMS SQUARE ROOT
    num = int(input("Enter number: "))
    print("The square root is %f" %(math.sqrt(num))) # %f converts the result to a float (decimal)

elif operation == "6": # SQUARE A NUMBER
    num = int(input("Enter number: "))
    print("The result is %d" %(pow(num, 2)))

else:
    print("Invalid Entry")