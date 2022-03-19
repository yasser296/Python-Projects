
import re
expr = "SYD-GW1 uptime is 1 year, 9 weeks, 2 days, 5 hours, 26 minutes"


p = re.compile(r'(\w+[-]\w+)\s.+((\d+\sy\w+),\s(\d+\sw\w+),\s(\d+\sd\w+),\s(\d+\sh\w+),\s(\d+\sm\w+))')
m = p.search(expr)
print(m.group(0))

print(m.group(1))

print(m.group(2))

print(m.group(3))


print(m.group(7))



print('######################################################################################\n\n\n')


p_named = re.compile(r'(?P<hostname>\w+[-]\w+)\s.+(?P<uptime>(?P<years>\d+\sy\w+),\s(?P<weeks>\d+\sw\w+),\s(?P<days>\d+\sd\w+),\s(?P<hours>\d+\sh\w+),\s(?P<minutes>\d+\sm\w+))')
m = p_named.search(expr)

print(m.group("minutes"))

print(m.group("uptime"))

print(m.group("hostname"))








