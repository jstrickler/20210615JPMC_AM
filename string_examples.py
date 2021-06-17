s1 = "spam\n"   # \n \r \t \f \b \\
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print(len(s1))
print(len(s2))
print(len(s5))
print(s1)
print(s2)
print("Done.")

print("It's a good thing")
print('It is a "good" thing')

print("""It's a "good" thing""")

print("""
select *
from animals
where common_name = 'wombat'
""")




