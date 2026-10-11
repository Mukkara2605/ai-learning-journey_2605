# Simple calculator (calculator.py): ask for two numbers and print the sum, difference, product, division and remainder, each in a clear f-string.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f" The sum of {num1} and {num2} is: {num1+num2}")
print(f" The difference of {num1} and {num2} is: {num1-num2}")
print(f" The product of {num1} and {num2} is: {num1*num2}")
print(f" The division of {num1} and {num2} is: {num1/num2}")
print(f" The remainder of {num1} and {num2} is: {num1%num2}")