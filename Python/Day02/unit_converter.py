# Unit converter (unit_converter.py): ask for kilometers, print miles using miles = km × 0.621371, rounded to 2 decimals.
km = float(input("Enter kilometers: "))
miles = km * 0.621371
print(f"{km} kilometers is equal to {miles:.2f} miles.")