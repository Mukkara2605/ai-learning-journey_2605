# Remove duplicates (dedupe.py): take [4, 2, 4, 7, 2, 9] and print the unique values in their original order.
numbers = [4, 2, 4, 7, 2, 9]
unique_nums = []
for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)
print(unique_nums)