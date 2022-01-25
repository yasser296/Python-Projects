from math import sqrt


VOH = 5 
VT0_driver = 1 
KR = 6        # KR = K_driver / K_load
VT0_load = -3 


# using numerical iteration, assuming Vout = 0 
# and substitute in the VT_load equation
# thus, VT_load = VT0_load

 
VT_load = VT0_load 
A = (VOH - VT0_driver)**2 - (1/KR)*abs(VT_load)**2 
VOL = VOH - VT0_driver - sqrt(A)

print("VOL at Vout = 0  thus, VT_load = VT0_load")
print("VOL = %f \n " % VOL )


# then take the value of VOL and 
# substitute in the VT_load equation
# thus, Vout = VOL

Vout = VOL 
alpha_F = 0.3 
gama = 0.4 
VT_load = VT0_load + gama*( sqrt(abs(2*alpha_F) + Vout) - sqrt(abs(2*alpha_F) ) )

print("VT_load at Vout = VOL")
print("VT_load = %f \n" % VT_load )



# Using this new value for VT_load, 
# We now recalculate VOL again for 5 times.

iteration_num = input("Enter the number of iterations : ")
print("\n")
for i in range( 1 , int( iteration_num ) + 1 ) :
	print("The iteration number %d :  " % i )
	A = (VOH - VT0_driver)**2 - (1/KR)*abs(VT_load)**2 
	VOL = VOH - VT0_driver - sqrt(A)

	print("VOL = %f  " % VOL )
	
	Vout = VOL 
	VT_load = VT0_load + gama*( sqrt(abs(2*alpha_F) + Vout) - sqrt(abs(2*alpha_F) ) ) 
	print("VT_load = %f \n" % VT_load )
	
	

"""
At this point, we can stop the iteration process 
since the threshold voltage of the load
 device 
has not changed in the two significant digits 
after the decimal point. Continuing the iteration 
would not produce a perceptible improvement of VOL.

"""