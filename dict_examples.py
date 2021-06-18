import sys

d1 = dict()  # empty dictionary
d2 = {}  # same

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}
airports['IAH'] = "Houston"
print(airports, '\n')
print(airports['OAK'])
airports['IAD'] = "Washington/Dulles"

for abbr in 'RDU', 'HOU', 'SAC', 'ELM', 'LGA':
    print(abbr, abbr in airports)
print()

print(airports.get('LGA'))
print(airports.get('LGA', "NOT FOUND"))

# airports[None] = "this is weird"
# print(airports[None])

# airports['XYZ'] = None
# airports[None] = None
print(f"{sys.maxsize:,d}")

print(airports.keys(), '\n')
print(airports.values(), '\n')

print(airports.items(), '\n')
# for k, v in D.items(): ...
for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(item):
    return item[1], item[0]

# for key, value in D.items(): ...
for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

