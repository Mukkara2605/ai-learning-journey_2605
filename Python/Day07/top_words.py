# Word frequency, top 3 (top_words.py): ask for a sentence, count how often each word appears, and print the 3 most frequent.
# Hint: count with counts[w] = counts.get(w, 0) + 1, then sort with sorted(counts.items(), key=lambda x: x[1], reverse=True).
sentence = input("Enter a sentence: ").lower()
words = sentence.split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for word, count in ranked[:3]:
    print(f"{word}: {count}")