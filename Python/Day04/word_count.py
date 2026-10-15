# Word counter (word_count.py): ask for a sentence and print the number of words and the longest word.
sentence = input("Enter a sentence: ")
word = sentence.split()
count = len(word)
longest_word = max(word, key=len)
print(count)
print(longest_word)