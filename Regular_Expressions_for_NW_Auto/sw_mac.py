sw_mac = '''pynetauto-sw01 84:3d:c6:05:09:11 
pynetauto-sw17 80:7f:f8:80:71:1b 
pynetauto-sw05 f0:62:81:5a:53:cd'''



### switch_MAC_string_without_re

# sw_mac = sw_mac.replace(":", "").upper() # Remove colons & capitalize
# list1 = sw_mac.split(" ") # Split items using whitespace & create list1

# list2 = [] # A new list 2
# for i in list1:
#     list2.append(i.strip()) # Remove whitespaces & add i(items) to list2

# sw = [] # sw list
# mac = [] # mac list
# for i in list2:
# 	if len(i) == 14: # If length of i is 14 (sw name), then add to sw list
# 		sw.append(i)
# 	if len(i) == 12: # If length of i is 12 (MAC), then add to mac list
# 		i = i[:6] + "******" # Replace last six hex to six *s
# 		mac.append(i)

# sw_mac_dict = dict(zip(sw, mac)) # Convert two lists into one dictionary
# for k,v in sw_mac_dict.items():
#     print(k, v) # print key & value on the same line




#########################################################################
#########################################################################
#########################################################################



### switch_MAC_string_with_re


import re # Import Python re (Regular Expression) module

sw_mac = sw_mac.replace(":", "").upper() # Remove colons & capitalize
pattern = re.compile("([0-9A-F]{6})" "([0-9A-F]{6})") # Create pattern to match
                                                      # macth 6 Hex numbers twice
print(pattern.sub("\g<1>******", sw_mac)) # Substitute group 1 pattern