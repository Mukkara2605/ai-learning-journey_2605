""" Assignment 2: Name cleaner (strings + sets)

File: clean_names.py

python
raw = ["  john SMITH ", "MARY    jones", "alex  Doe", "john smith", "  Mary Jones"]

Tasks:

Clean every name: strip, collapse extra spaces, title-case.
Print the cleaned list.
Print the unique cleaned names in alphabetical order.
Print how many duplicates were removed."""

raw = ["  john SMITH ", "MARY    jones", "alex  Doe", "john smith", "  Mary Jones"]
cleaned = [name.strip().replace("  ", " ").title() for name in raw]
unique = sorted(set(cleaned))
duplicates_removed = len(cleaned) - len(unique)

print("Cleaned names:")
for name in cleaned:
    print(f"  {name}")

print(f"\nUnique cleaned names in alphabetical order:")
for name in unique:
    print(f"  {name}")

print(f"\nNumber of duplicates removed: {duplicates_removed}")