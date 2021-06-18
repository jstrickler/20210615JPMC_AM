#!/usr/bin/env python
from collections import Counter
with open("../DATA/breakfast.txt") as breakfast_in:
    items = (line.rstrip() for line in breakfast_in)

    counts = Counter(items)
    counts['pancakes'] += 1
    print(counts)
    print(counts['roti'])
    print(counts.most_common())

with open('../DATA/words.txt') as words_in:
    first_letters = (word[0] for word in words_in)

    wcounts = Counter(first_letters)
    print(wcounts.most_common())
