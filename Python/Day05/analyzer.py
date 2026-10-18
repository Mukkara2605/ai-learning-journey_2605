# Number and text analyzer (analyzer.py): ask for a sentence, then print
#the number of words
#the longest word
#the number of vowels
#whether the whole sentence is a palindrome (ignoring spaces and case)

sentence = input("Enter a sentence: ")
words = sentence.split()
number_of_words = len(words)
longest_word = max(words, key=len)
vowels = "aeiouAEIOU"
number_of_vowels = sum(sentence.count(vowel) for vowel in vowels)
is_palindrome = sentence.replace(" ", "").lower() == sentence.replace(" ", "").lower()[::-1]
print(number_of_words)
print(longest_word)
print(number_of_vowels)
print(is_palindrome)    