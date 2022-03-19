import re

expr = "downupupupdowndownupdowndown"
p = re.compile("(up)+")
m = p.search(expr)
print(m)
print(m.group(0))


print('######################################################################################\n\n\n')


expr = "United States 1 408 526 1234"
p = re.compile(r"\w+\s\w+\s\d\s\d{3}\s\d{3}\s\d+")
m = p.search(expr)
print(m)

print('######################################################################################\n\n\n')

expr = "United States 1 408 526 1234"
p = re.compile(r"(\w+\s\w+)\s\d?\s\d{3}\s\d{3}\s\d+")
m = p.search(expr)
print(m)
country = m.group(1)
print(country)

print('######################################################################################\n\n\n')
 
expr = "United States 1 408 526 1234"
p = re.compile(r"(\w+\s\w+)\s(\d?\s\d{3}\s\d{3}\s\d+)")
m = p.search(expr)
print(m)
phone_number = m.group(2)
print(phone_number)

print('######################################################################################\n\n\n')

expr = "United States 1 408 526 1234"
p = re.compile(r"(\w+\s\w+)\s((\d?)\s(\d{3})\s(\d{3}\s\d+))")
m = p.search(expr)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
print(m.group(5))

print('######################################################################################\n\n\n')


expr = "Did you know that that 'that', that that person used in that sentence, is wrong."
p = re.compile(r'(\bthat)\s+\1')
m = p.search(expr)
print(m)
m = p.search(expr).group()
print(m)
