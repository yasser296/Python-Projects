import re


print(re.findall('^S.+sh', 'Start to finish'))

print(re.findall('\AS.+sh', 'Start to finish'))

print('######################################################################################\n\n\n')


print(re.findall('^S.+sh', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))

print(re.findall('\AS.+sh', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))

print('######################################################################################\n\n\n')


print(re.findall('S.+sh$', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))

print(re.findall('S.+sh\Z', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))
print('######################################################################################\n\n\n')

print(re.findall('^S.+sh$', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))

print(re.findall('\AS.+sh$', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))
print('######################################################################################\n\n\n')

print(re.findall('^S.+sh\Z', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))

print(re.findall('\AS.+sh\Z', 'Start to finish\nSuper special fish\nSuper fresh fish\nSuper smelly fish', re.M))
