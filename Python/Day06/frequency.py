# Frequency counter (frequency.py): ask for a sentence and print how many times each word appears.
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1 
    else:
        frequency[word] = 1
for word, count in frequency.items():
    print(f"{word}: {count}")
