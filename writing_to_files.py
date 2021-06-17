
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

# modes:  r w a x
with open('fruits.txt', 'a') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

with open('DATA/words.txt') as words_in:
    with open('qwords.txt', 'w') as words_out:
        for line in words_in:
            if 'q' in line:
                words_out.write(line)

