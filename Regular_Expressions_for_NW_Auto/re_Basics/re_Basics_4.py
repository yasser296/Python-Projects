import re 

expr = 'a\nb'

p = re.compile('a.b')
m = p.match(expr)
print(m)


p = re.compile('a.b', re.DOTALL)
m = p.match(expr)
print(m)


print('######################################################################################\n\n\n')


import re
expr1 = 'automation'
expr2 = 'Automation'
expr3 = 'AUTOMATION'

p = re.compile('[a-z]+', re.IGNORECASE)

m1 = p.match(expr1)
print(m1)

m2 = p.match(expr2)
print(m2)

m3 = p.match(expr3)
print(m3)



print('######################################################################################\n\n\n')



import re
expr = '''Regular Engineers
Regular Network Engineers
Regular but not so regular Engineers'''

p = re.compile('^R\w+\S')
m = p.findall(expr)
print(m)

p = re.compile('^R\w+\S', re.MULTILINE)
m = p.findall(expr)
print(m)



print('######################################################################################\n\n\n')




# Example1 – without re.VERBOSE
import re

expr = 'I was born in 2,009 and I am 15 years old. I started my primary school in 2,010'

p = re.compile(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0')
m = p.findall(expr)

print(m)



# Example2 – with re.VERBOSE

p = re.compile(r"""
[1-9]           # Match a single digit between 1-9
(?:\d{0,2})     # Match digit equatl to [0-9] between 0 and 2 times
(?:,\d{3})*     # Match the character ,(Comma) literally, match a digit equal to [0-9] \
                  exactly 3 times) Zero and unlimited times
(?:\.\d*[1-9])? # Match the character. (Dot) literally, match a digit equal to [0-9] \
                   zero and unlimited times, match a single digit between [1-9]) \
                   zero and one time.
|               # OR
0?\.\d*[1-9]    # Match 0 zero or one time, match . (Dot) literally, match a digit \ 
                   equal to [0-9] zero or unlimited times, and match a digit between [1-9]
|               # OR
0               # Match one 0
""", re.VERBOSE)

m = p.findall(expr)

print(m)






