
import re
expr = "+1 408 526 1234"
p = re.compile(r"((?:(\+1)[ -])?\(?(\d{3})\)?[ -]?\d{3}[ -]?\d{4})")
m = p.search(expr)
print(m)

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))





