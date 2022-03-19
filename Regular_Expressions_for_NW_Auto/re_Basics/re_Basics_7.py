import re

print(re.findall('^Start', 'Start to finish'))
print(re.findall('^Sta\w+', 'Start to finish'))


print('######################################################################################\n\n\n')

print(re.findall('finish$', 'Start to finish'))
print(re.findall('fin\w+$', 'Start to finish'))


print('######################################################################################\n\n\n')


print(re.findall('^S.+sh$', 'Start to finish'))

print('######################################################################################\n\n\n')


print(re.findall('^S.+sh$', 'Start to finish\nSpecial fish\nSuper fresh', re.MULTILINE))

print('######################################################################################\n\n\n')




expr = '''
SYDCBDPIT-ST01#sh ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  unassigned      YES NVRAM  up                    up
Vlan50                 10.50.50.11    YES NVRAM  up                    up
FastEthernet0          unassigned      YES NVRAM  down                  down
GigabitEthernet1/0/1   unassigned      YES unset  down                  down
GigabitEthernet1/0/2   unassigned      YES unset  up                    up
GigabitEthernet1/0/3   unassigned      YES unset  up                    up

		'''

p = re.compile('^Gig.+down$', re.MULTILINE)
m = p.findall(expr)
print(m)
