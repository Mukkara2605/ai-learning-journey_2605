# Palindrome checker (palindrome.py): print whether a word reads the same backwards. Ignore upper or lower case.
word = input("Enter a word: ")
if word.lower() == word[::-1].lower():
    print("Palindrome")
else:
    print("Not a palindrome")