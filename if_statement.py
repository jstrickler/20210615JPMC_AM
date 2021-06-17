value = 56

# if elif else while for def class with try except finally

if value > 75:  #  if bool(value > 75) == True:
    print("wombat")
    print("koala")
    if value > 80:
        print("kookaburra")
elif value > 50:  # else if

    print("kangaroo")
    print("quokka")

else:

    print("wildebeest")
    print("zoril")


print("Done.")

# X is False if
#   X == False
#   X == None
#   X == 0 or X == 0.0
#   len(X) == 0
#     ""
#     [] () {}

#  == != > < >= <=

x = 10
if x:
    print("whooopeeeee")

y = 0
if not y:
    print("ok, then")

# Don't say this:
# if bool(x) == True:  # is x equal to integer value 1
# Say this:
if x:
   print('Not common')

print(int(True), int(False))

debug = True
#          A?B:C
# color = debug?'red':'blue';   # java

#    B if A else C
color = 'red' if debug else 'blue'  # python ternary operator
if debug:
    color = 'red'
else:
    color = 'blue'

print("color:", color)
# and or not

if (x > 5) and debug:
    print("Wooly Worm")

if x > 1000 or color == 'red':
    print("Honey badger")

# PEMDAS Please Excuse My Dear Aunt Sally

default = 100
user_input = 0

value = user_input or default
print(value)
