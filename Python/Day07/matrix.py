''' 5. Matrix sum (matrix.py): given [[1, 2, 3], [4, 5, 6], [7, 8, 9]], print the sum of each row and the sum of all numbers.
Hint: a nested loop, or sum() on each inner list. '''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grand_total = 0

for row in matrix:
    row_sum = sum(row)
    print(f"Sum of row {row}: {row_sum}")
    grand_total += row_sum

print(f" Sum of all numbers: {grand_total}")
