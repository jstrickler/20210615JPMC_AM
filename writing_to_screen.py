x = 5
y = 'wombat'
z = 4.239043923

print(x, y, z)
print(str(x), str(y), str(z))

print(x, y, z, sep='')
print(x, y, z, sep=':')

name = "john jacob jingleheimer smith"
print(name.count('j'))



print(x)
print(y)
print(z)
print(x, end=" ")
print(y, end=" ")
print(z)
print()


print(f"{z:.2f}")  # newest  (python 3.6 and later)
print("{:.2f}".format(z))  # python 3.0 and later
print("%.2f" % (z))  # python 2 legacy

print(x, y)
print(f"{x} {y}")
print("{} {}".format(x, y))

# " "  r" "  f" "

name = "Bob"
city = "Trenton"
state = "NJ"
print(f"{name} lives in {city}, {state}")
print("{} lives in {}, {}".format(name, city, state))
# print(name, "lives in", city, ",", state)

print(f"2 + 2 is {2 + 2}")

