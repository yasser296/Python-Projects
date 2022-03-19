import re


expr = "Small computers include smartphones."
p = re.compile(r'\bcomputers\b')
m = p.search(expr)
print(m)


expr = "Microcomputers include smartphones."
p = re.compile(r'\bcomputers\b')
m = p.search(expr)
print(m)


expr = "Microcomputers include smartphones."
p = re.compile(r'computers\b')
m = p.search(expr)
print(m)


expr = "Microcomputers include smartphones."
p = re.compile(r'\Bcomputer\B')
m = p.search(expr)
print(m)
