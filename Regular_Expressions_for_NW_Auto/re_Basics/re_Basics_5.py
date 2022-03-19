# Ex1 - backslashes without raw string notation (r)
import re
expr = 'Our team \scored three goals\\'
p1 = re.compile('\scored')
p2 = re.compile('\\scored')
p3 = re.compile('\\\scored')
p4 = re.compile('\\\\scored')
p5 = re.compile('\\\\\scored')
print(p1.findall(expr))

print(p2.findall(expr))

print(p3.findall(expr))

print(p4.findall(expr))

print(p5.findall(expr))

print('######################################################################################\n\n\n')


# Ex2 – backslash with raw string notation (r)
import re
expr = 'Our team \scored three goals\\'
p1 = re.compile(r'\scored')
p2 = re.compile(r'\\scored')
p3 = re.compile(r'\\\scored')
p4 = re.compile(r'\\\\scored')
print(p1.findall(expr))

print(p2.findall(expr))

print(p3.findall(expr))

print(p4.findall(expr))



print('######################################################################################\n\n\n')


# Ex3 – backslash with raw string notation (r)
import re
expr = 'Our team \scored three goals\\'
p2 = re.compile(r'\\scored')
m = p2.findall(expr)
print(m)
n = m[0]
print(n)
for x in n:
    print(x, end="")



