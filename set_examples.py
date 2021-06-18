c1 = ['red', 'green', 'green', 'blue', 'purple', 'brown', 'orange']
c2 = ['blue', 'brown', 'brown', 'brown', 'green', 'yellow', 'lavender']
set1 = set(c1)
set2 = set(c2)

set1.add('chartreuse')
set2.add('mauve')

print("set1:", set1)
print("set2:", set2)
print()

print("common:", set1 & set2)  # intersection
print("not common:", set1 ^ set2)  # xor
print("both:", set1 | set2)  # union

common_items = sorted(set1 & set2)
print(common_items)