sentence = input("Enter a sentence: ")
sentence = sentence.split()
for i in range(len(sentence)):
    sentence[i] = sentence[i].capitalize()

print("".join(sentence))
