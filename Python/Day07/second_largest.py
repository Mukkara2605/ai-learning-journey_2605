# Second-largest without sort (second_largest.py): find the second-largest number in a list using a loop and two variables, not sorted().
numbers = [10, 5, 8, 12, 3, 15, 7]

largest = float("-inf")
second = float("-inf")

for n in numbers:
    if n > largest:
        second = largest       # the old largest moves down
        largest = n     # the new number takes the top
    elif n > second and n != largest:
        second = n

print(f"Second largest: {second}")