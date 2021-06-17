fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    if f.startswith('p'):
        f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits if f.startswith('p')]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits]
print("f2:", f2, '\n')

#  [EXPR for VAR in ITERABLE if CONDITION]
f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print(f"last_names: {last_names}\n")

# "{} {}".format(p[0], p[1])
full_names = [f"{p[0]} {p[1]}" for p in people]
print("full_names:", full_names, '\n')

numbers = [5, 8, 22, 1, 13]
halves = [n/2 for n in numbers]
print(f"halves: {halves}")

dirty_s = ['foo\n', 'bar\n', 'blah\n']
clean_s = [s.rstrip() for s in dirty_s]
print(dirty_s)
print(clean_s)

print(dirty_s[0])
print(repr(dirty_s[0]))
print(repr(clean_s[0]))

fruits_upper = [f.upper() for f in fruits]
print("fruits_upper:", fruits_upper, '\n')

fgen = (f.upper() for f in fruits)
print(fgen)
fruits.append('durian')
fruits.append('jackfruit')

for fruit in fgen:
    print(fruit)




