fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[-1], fruits[-4])
print(fruits[0], fruits[len(fruits)-1], fruits[len(fruits)-4])

print(fruits[0:4])  # 0-3
#  inc    exc
#  [start:stop]
print(sorted(fruits[9:14], reverse=True))  # 9-13

#       012345678901234
name = "Walter Winchell"
print(name[7:10])  # 7-9
n2 = name[:]
print(fruits[9:14].sort())
x = fruits[9:14]
x.sort()
print(x)
print()

print(fruits[3:12])
print(fruits[3:12:2])
print(fruits[3:12:3])
print()

# iterables: list tuple str bytes dict set generator range

for fruit in fruits:
    # fruit = <next element of fruits>
    print(fruit.upper())
print()

for wombat in fruits[:3]:
    print(wombat.title())


print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits))
print('-' * 60)

rfruits = reversed(fruits)
print(rfruits)  # GENERATOR!!
for fruit in rfruits:
    print(fruit)
print()

actor = "Chris Hemsworth"
for char in reversed(actor):
    print(char, end='')
print('\n')

colors = ['red', 'green', 'purple', 'black', 'brown']
numbers = [5, 3, 8, 7, 2, 6, 1, 8, 19, 4]
result = zip(colors, numbers)
print(result)
print(list(result))
print(list(result))
result = zip(colors, numbers)
for color, number in result:
    print(color * number)
print()

for i, fruit in enumerate(fruits):  #  [(index, obj), (index, obj), ...]
    print(i, fruit)
print()

s = set(['a', 'b', 'c'])

for i, item in enumerate(s):
    print(i, item)
print()

junk = ['do', 're', 'me']
print(junk * 3)

flags = ['False'] * 10
print(flags)

nums = [0] * 20
print(nums)
print()

for f in 'apple', 'durian', 'banana', 'marionberry':
    print(f, f in fruits)
print()

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = a + b
print(c)

a = "Lee"
b = "loo"
c = a + b
print(c)

