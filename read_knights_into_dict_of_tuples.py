from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

print(knight_info, '\n')

pprint(knight_info, sort_dicts=False)  # sort_dicts 3.8+
print()

print(knight_info['Arthur'], '\n')
print(knight_info['Arthur'][0], '\n')

for knight, info in knight_info.items():
    print(info[0], knight)

