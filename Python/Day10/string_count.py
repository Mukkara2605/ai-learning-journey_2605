# Count how many times each letter appears in a sentence
sentence = input("Enter a sentence: ")
letter_count = {}
for letter in sentence:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter]+= 1
        else:
            letter_count[letter] = 1
for letter, count in sorted(letter_count.items()):
    print(f"{letter}: {count}")