# Vowel and consonant counter (vowels.py): ask for a word and print how many vowels and consonants it has.
word = input("Enter a word: ")
vowels = 0
consonants = 0
for char in word:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")