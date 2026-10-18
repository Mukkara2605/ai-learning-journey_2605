#Multiplication table (table.py): ask for a number and print its table from 1 to 10, like 7 x 3 = 21.
#Hint: a for loop with range(1, 11) and an f-string.

number = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{number}*{i} = {number * i}")