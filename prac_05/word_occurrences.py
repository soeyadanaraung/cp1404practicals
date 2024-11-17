"""
Word Occurrences
"""

word_to_count = {}

text = input("Text: ")
words = text.split()
words.sort()

max_length = max(len(word) for word in words)

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")