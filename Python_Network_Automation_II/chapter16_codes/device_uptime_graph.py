import matplotlib.pyplot as plt # import matplotlib library
import pandas as pd  # import pandas library
from prettytable import PrettyTable

device_uptime = {	'LAB-R1': 6.87, 
				 	'LAB-SW1': 6.87, 
				 	'Lab-SW4': 12.23, 
				 	'Lab-sw3': 10.22, 
				 	'lab-r2': 12.2, 
				 	'lab-sw2': 10.65
				}
# Resulting dictionary from step 15

df = pd.DataFrame(list(device_uptime.items()),columns = ['host','uptime']) # Convert dictionary into pandas dataframe with column titles ‘host’ & ‘uptime’

print(df)

df.plot(kind='bar',x='host',y='uptime') # Plot a bar graph with host as x-axis and uptime(float) as y-axis
plt.show() # Display graph 


m1 = ['R1', 'SW3'] 
uptime = [0.02, 0.17]

table = PrettyTable(['host','uptime'])
table.align = 'l'

for item in range(len(uptime)):
    table.add_row([ m1[item] , uptime[item] ])

print(table)
