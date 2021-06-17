x = 5    # 'x' is *bound* to python *object*
y = 10
result = x + y
print(result)

#  a-z A-Z 0-9 _

# local variables and  functions:   lower_case_words_with_underscores
# global variables:  UPPER_CASE_WORDS
# classes:  UpperCamelCase

# "private": _leading_underscore

spam = 12
ham = "wombat"

x = None
print(x)

def foo(m):
    if m is not None:
        pass
        # blah
    else:
        pass
        # other blah

print(type(x))

x = 5  # create int object and bind obj to "x"
x = 4  # create NEW int obj ...
x = "hello"   # create str obj and bind to "x"
x = None  # etc etc
x = 4.2

a = 10  # create int and bind 'a'
b = a   # bind 'b' to same obj as 'a'
print(a, b)
a = 1000  # create new obj and bind to 'a'
print(a, b)

# id, min, max, file, open, dir,

# string = new string("Hello");

x = 123456665
import sys
print(sys.getsizeof(x))

# int i;
# i = 10;

a = "apple"
b = "123"
print(type(a), type(b))
print(a + b)
print(b * 10)
print("-" * 60)





