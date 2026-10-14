# Pattern (pattern.py): use nested loops to print a triangle of stars with 5 rows.
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()