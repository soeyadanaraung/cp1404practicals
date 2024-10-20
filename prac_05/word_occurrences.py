"""
Word Occurrences
Estimate: 15 minutes
Actual:   30 minutes
"""

word_to_count = {}

text = input("Text: ")
words = text.split()
words.sort()
maximum_length = max(len(word) for word in words)

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in word_to_count.items():
    print(f"{word:{maximum_length}} : {count}")