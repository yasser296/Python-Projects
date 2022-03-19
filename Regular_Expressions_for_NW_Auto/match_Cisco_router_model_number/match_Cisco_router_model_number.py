import re

sh_ver_file = open("E:/python_projects/Regular_Expressions_for_NW_Auto/match_Cisco_router_model_number/sh_ver2.txt")
read_file = sh_ver_file.read()

### Only match Cisco router model number from show version output.
rt_model = re.findall("[A-Z]{3}\d{4}[/]\w+", read_file)
'''
	[A-Z]{3} or \w\D[^a-z]	: three capital letters
	\d{4} or [0-9]{4}  	: four digits
	[/] 		: character "/"
	\w+ [0-9a-zA-Z]{2}		: any string with at least one occurrence
'''



print(rt_model)
my_router = rt_model[0]
print(my_router)

