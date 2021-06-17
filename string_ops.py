actor = "Chris Hemsworth"

print(actor)
print(len(actor))

print(actor.upper())
actor.upper()
print(actor)
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.count('h') + actor.count('H'))
print(actor.index('ris'))
print(actor.find('ris'))

x = "123abc"
print(x.isalpha(), x.isnumeric(), x.isalnum())
y = "   \t\t   "
print(y.isspace())

s = "     I am the kumquat Haagen-Daaz    "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = "qagggumI am the kumquat Haagen-Daaztkuqqqqmquat"
print('|' + s.lstrip('tkuqgma') + '|')
print('|' + s.rstrip('tkuqgma') + '|')
print('|' + s.strip('tkuqgma') + '|')
print()

x = "foo-------"
print(x.rstrip('-'))

line = "spam spam spam\n"
print(line.rstrip())

record = "a;123;wombat;Goa"
print(record.split(';'))

words = "    Avengers            assemble!     "
print(words.split())

# cursor.execute("select * from spam")









