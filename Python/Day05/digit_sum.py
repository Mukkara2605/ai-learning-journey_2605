#digit sum (digit_sum.py): ask for a number such as 1234 and print the sum of its digits (10).
#Hint: keep the input as text, loop over each character, and convert with int().
number = input("Enter a number:")
sum = 0
for digit in number:
    sum = sum + int(digit)

print(f"Sum of Digits of {number} is {sum}")