from numpy import arange
from matplotlib import pyplot , figure

# Kn = Kn' * W/L 4
Kn=1e-3 
# Vth is th threshold voltagee 
Vth = 1.5
# Sweep drain to source voltge from 0 to 12V  
Vds = arange(0, 12, 0.1).tolist()
Vgs = [4 , 6 , 8 , 10 ] 
Id = list()   #  Drain Current Id (A)
for I in range(1,len(Vgs)+1) :
	Id.append([])
	
print(Id)
print("\n\n\n\n\n")

# To draw the transition line
line_Id = list()
line_Vds = list()

# Estimate length of the Vds & Vgs lists
m = len( Vds ) 
n = len( Vgs )

# Initialize the I-V characteristic points
for i in range(0,n) :
	for j in range(0,m) :
		if (Vgs[i] < Vth) :
			Id[i].append(0)
			
		elif (Vds[j] >= ( Vgs[i] - Vth )) :
			Id[i].append((0.5 * Kn * (Vgs[i] - Vth)**2) * 1000)
			
		elif (Vds[j] < ( Vgs[i] - Vth )) :
			Id[i].append((Kn *( (Vgs[i] - Vth)* Vds[j] - 0.5 * (Vds[j]**2) )) * 1000 )
		
		# get the transition line points
		if (Vds[j] == ( Vgs[i] - Vth )) :
			line_Id.append((0.5 * Kn * (Vgs[i] - Vth)**2) * 1000 )
			line_Vds.append(Vds[j])
			
print(Id)


# Plotting the I-V characteristic of n-MOSFET
figure, axis = pyplot.subplots()
print(axis)
print(figure)
figure.set_size_inches(12, 8)
print(figure)


curves = list()
for i in range(0,len(Vgs)) :
	curve, = pyplot.plot(Vds, Id[i] , label="Vgs= %d" %Vgs[i] , linewidth=2)
	pyplot.annotate("Vgs= %d" %Vgs[i], (10, max(Id[i])+0.0005) , fontsize=12 )
	curves.append(curve)


# Plotting the transition line
line_Vds_2 = [0] + line_Vds
line_Id_2 = [0] + line_Id
tran, = pyplot.plot(line_Vds_2 , line_Id_2 , label="Transition line" , linestyle='--' , marker= 'x' , markersize = 12 )
curves.append(tran)

# Plotting the legends
pyplot.legend (curves, [curve.get_label() for curve in curves] , prop={"size":12})
# or 
# #fontsize=16  ==   prop={"size":16}   on legend only



axis.set_xlabel("Drain-source voltage Vds (Volt)" , fontsize=16 )
axis.set_ylabel("Drain Current Id (mA)" , fontsize=16 )

pyplot.grid(linestyle='--')
#pyplot.xaxis.grid (color="g")
#pyplot.yaxis.grid (color="r")

Vds_x_axis_numbers = arange(0,13,0.5).tolist()
axis.set_xticks (Vds_x_axis_numbers)
axis.tick_params ( axis='x' , colors='b')

Id_y_axis_numbers = arange(0,41,1).tolist()
axis.set_yticks (Id_y_axis_numbers)
axis.tick_params ( axis='y' , colors='g')


pyplot.title("I-V Characteristics of a n-MOSFET" ,fontsize=16 )

resolution = 500
pyplot.savefig('I-V_characteristic_dpi=%d' %resolution , dpi=resolution)


pyplot.show()









