from collections import namedtuple, defaultdict

person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(person, type(person), person[0])

people = []
people.append(person)
print(people)
person = ('Larry', 'Wall', 'Perl', '1954-09-27')
# x = 5; y = 6; z = 7
people.append(person)
print(people)
print(person[1])

Person = namedtuple("Person", "first_name last_name product dob")

p1 = Person('Bill', 'Gates', 'Microsoft', '1955-10-24')
print(p1.first_name, p1.last_name)

print(Person.__name__)
print(type(p1).__name__)

values = [1, 2, 3, 4, 5]
a, b, *c = values   # unpacking
print(a, b, c)
a, *b, c = values   # unpacking
print(a, b, c)
*a, b, c = values   # unpacking
print(a, b, c)

print(person)
first_name, last_name, product, dob = person
print(last_name, product)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', 'MySQL', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
print()

data = [('red', 5), ('purple', 6), ('purple', 3), ('black', 1),
        ('red', 2), ('red', 3)]

for color, number in data:
    print(color, number)
print()

colors = ['purple', 'blue', 'purple', 'purple', 'green']
c = set(colors)
print(c)
c.add('blue')
print(c)

data = [('red', 5), ('purple', 6), ('purple', 3), ('black', 1),
        ('red', 2), ('red', 3)]

color_info = defaultdict(list)
for color, number in data:
    color_info[color].append(number)
print(color_info)
cc = dict(color_info)
print(cc)
print(color_info['red'])
print(color_info['red'][1])
print(color_info[0])




















