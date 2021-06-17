list1 = list() # new, empty list
list2 = ['red', 'blue', 'green']  # assign literal list
print(list2[0])
list3 = []  # shortcut for empty list

cities = ['Plano', 'Chicago', 'Durham', 'Trenton',
          'New York']

cities.append("Columbus")
print(cities)
cities.append("Tampa")
print(cities)
cities.insert(0, "Houston")
print(cities)
cities.insert(5, "Raleigh")
print(cities)
more_cities = ["Red Bank", "Toledo", "Schaumberg"]
cities.extend(more_cities)
print(cities)
print(len(cities))

# L.append(item) L.extend(iterable) L.insert(pos, item)

del cities[9]
print(cities)

cities.remove('Trenton')
print(cities)

cities[4] = "Cary"
print(cities)
# cities[20] = "Pittsburgh"

c = cities.pop()  # remove last element
print(c)
print(cities)

c = cities.pop(4)
print(c)
print(cities)

#  del L[n]    L.remove(value)  L.pop()  L.pop(pos)
print(cities[0])
print(cities[3])
print(cities[-1])
print(cities[-3])
x = "abc"
print(x[0], x[-1])

print(cities)
#  cities[start:stop]
print(cities[0:3])
print(cities[5:7])
print(cities[5:-1])
print(cities[2:-2])
print(cities[:3])
print(cities[4:])
print(cities[-3:])
s = "Mississippi"
print(s[7:10])
print(cities[4:99])
print(cities[99:4])
print(cities[22:])






