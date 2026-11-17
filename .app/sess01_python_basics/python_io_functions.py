# Python file to demonstrate input and output functions in python

# Prompt/request the user to enter their name
print("Please enter your name")
name = input()

# Display the user's name
print(f"Hello {name} from python IO functions")

# Request the user for 2 numbers
num1 = int(input("Please enter the first number: \n"))
num2 = int(input("Please enter the second number: \n"))

sum = num1 + num2
print(f"The sum of {num1} + {num2} is {sum}")