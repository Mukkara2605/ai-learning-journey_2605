#Reverse each word (reverse_words.py): turn I love Python into I evol nohtyP.
# Hint: split(), reverse each word with [::-1], then " ".join(...).
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word[::-1], end=" ")