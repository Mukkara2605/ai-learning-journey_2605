# Anagram checker (anagram.py): ask for two words and print whether they use the same letters.
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if sorted(word1.lower()) == sorted(word2.lower()):
    print("Anagrams")
else:
    print("Not anagrams")
    