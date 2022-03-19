import os
import re
import pandas as pd # import pandas
from prettytable import PrettyTable


show_ver = os.popen('genie parse "show version" --testbed-file testbed.yml --devices[hostname]')

output = show_ver.read()
print(output , "\n\n\n")

print("the type of the output is: " , type(output) , "\n\n\n")

p1 = re.compile(r'(?<=\"hostname\": \").+(?=\")')
m1 = p1.findall(output)
print(m1 , "\n\n\n")

p2 = re.compile(r'(?<=\"uptime\": \").+(?=\")')
m2 = p2.findall(output)
print(m2 , "\n\n\n")

##### If the devices are running more than 1 hr #####
#uptime = [] # create empty list called uptime
#for x in m2: # for loop to call out each item in list m2
#    y = [int(s) for s in x.split() if s.isdigit()] # If string is a digit, then save it as y
#
#    z = (y[1]/60) # y[1] or the second number from y is minute value, divide it by 60 minutes and convert it into a decimal points
#
#    a = round(y[0] + z, 2) # y[0] or the first number from y is hour value, combine it with z, then roud it to 2 decimal places
#    uptime.append(a) # append the value a to uptime list

#print(uptime) # print the result of uptime list

##### If your devices’ uptime is less than 60 minutes #####
uptime = []
for x in m2:
    y = [int(s) for s in x.split() if s.isdigit()]
    z = (y[0]/60)
    a = round(z, 2)
    uptime.append(a)

print(uptime)

print("\n\n\n")

device_uptime = dict(zip(m1,uptime)) # Combine m1 and uptime lists and make them into a dictionary
print(device_uptime , "\n\n\n") # display device_uptime dictionary

### Let’s use the pandas module to turn the dictionary into a 
### pandas dataframe and save it as an Excel spreadsheet for reporting purposes.
df = pd.DataFrame(list(device_uptime.items()),columns = ['host','uptime'])
print(df , "\n\n\n")

df.to_excel('device_uptime.xlsx') # Write data frame to excel using panda's to_excel feature.



table = PrettyTable(['host','uptime'])
table.align = 'l'

for item in range(len(uptime)):
    table.add_row([ m1[item] , uptime[item] ])

print(table)

