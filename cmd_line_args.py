import sys
import hermodule
from hermodule import doit

print(sys.argv)

print("script name:", sys.argv[0])
print("first arg:", sys.argv[1])
hermodule.doit()
doit()
