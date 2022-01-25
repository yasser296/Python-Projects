from tkinter import *
from tkinter import filedialog

master = Tk()
master.geometry("700x700")
master.configure(bg='#000000')

a = 70

# To capture the mouse coordinates
# Just to arrange the frames in the suitable place
def coordinates(event):
	print("Mouse Coordinates: " + str(event.x) + " , " + str(event.y))

master.bind("<Button-1>", coordinates) # Left mouse click
# master.bind("<Enter>", coordinates) # when entering to the frame
# master.bind("<Motion>", coordinates) # motion of the mouse 



frame_select_path = Frame(master , bd = 10 , bg = "#CA6B45")
frame_select_path.place(x=10, y=10)

label_select_path = Label(frame_select_path  , fg = "blue" , text="Select Path: " , bd = 10)
label_select_path.pack(side=LEFT)

entry_select_path = Entry(frame_select_path, width = 70 , bd = 10)
entry_select_path.pack(side=RIGHT)

def select_path():
	path = filedialog.askdirectory(initialdir="/", title="Select file" )
	entry_select_path.delete(0,200)
	entry_select_path.insert(0,path)
	print(path)



frame_button_select = Frame(master , bd = 10 , bg = "#CA6B45")
frame_button_select.place(x=560, y=10)

button_select = Button( frame_button_select, text = " Select Path ", 
						command = select_path ,
			 			fg = "black", font = "Times", 
			 			bg = "light blue" )
button_select.pack()



frame_user_name = Frame(master , bd = 10 , bg = "green")
frame_user_name.place(x=10, y=10+a)

label_user_name = Label(frame_user_name  , fg = "blue" , text="User Name: " , bd = 10)
label_user_name.pack(side=LEFT)

entry_user_name = Entry(frame_user_name, width = 20 , bd = 10)
entry_user_name.pack(side=RIGHT)



frame_PW = Frame(master , bd = 10 , bg = "green")
frame_PW.place(x=10, y=70+a)

label_PW = Label(frame_PW  , fg = "blue" , text="Password: " , bd = 10)
label_PW.pack(side=LEFT)

entry_PW = Entry(frame_PW, width = 20 , bd = 10)
entry_PW.pack(side=RIGHT)



frame_enable_PW = Frame(master , bd = 10 , bg = "#FF3400")
frame_enable_PW.place(x=10, y=140+a)

label_enable_PW = Label(frame_enable_PW  , fg = "blue" , text="Enable PW: " , bd = 10)
label_enable_PW.pack(side=LEFT)

entry_enable_PW = Entry(frame_enable_PW, width = 20 , bd = 10)
entry_enable_PW.pack(side=RIGHT)



frame_IP = Frame(master , bd = 10 , bg = "blue")
frame_IP.place(x=10, y=210+a)

label_IP = Label(frame_IP  , fg = "blue" , text="IP: " , bd = 10)
label_IP.pack(side=LEFT)

entry_IP = Entry(frame_IP, width = 20 , bd = 10)
entry_IP.pack(side=RIGHT)



frame_mask = Frame(master , bd = 10 , bg = "blue")
frame_mask.place(x=220, y=210+a)

label_mask = Label(frame_mask  , fg = "blue" , text="Mask: " , bd = 10)
label_mask.pack(side=LEFT)

entry_mask = Entry(frame_mask, width = 20 , bd = 10)
entry_mask.pack(side=RIGHT)



frame_port_type = Frame(master , bd = 10 , bg = "#F129C0")
frame_port_type.place(x=10, y=280+a)

label_port_type = Label(frame_port_type  , fg = "blue" , text="Port Type: " , bd = 10)
label_port_type.pack(side=LEFT)

entry_port_type = Entry(frame_port_type, width = 10 , bd = 10 )
entry_port_type.pack(side=RIGHT)



frame_port_num = Frame(master , bd = 10 , bg = "#F129C0")
frame_port_num.place(x=220, y=280+a)

label_port_num = Label(frame_port_num  , fg = "blue" , text="Port Number: " , bd = 10)
label_port_num.pack(side=LEFT)

entry_port_num = Entry(frame_port_num, width = 10 , bd = 10 )
entry_port_num.pack(side=RIGHT)



frame_Host_Name = Frame(master , bd = 10 , bg = "#110334")
frame_Host_Name.place(x=10, y=340+a)

label_Host_Name = Label(frame_Host_Name  , fg = "blue" , text="Host Name: " , bd = 10)
label_Host_Name.pack(side=LEFT)

entry_Host_Name = Entry(frame_Host_Name, width = 50 , bd = 10 )
entry_Host_Name.pack(side=RIGHT)



frame_MOTD = Frame(master , bd = 10 , bg = "#00C4FF")
frame_MOTD.place(x=10, y=410+a)

label_MOTD = Label(frame_MOTD  , fg = "blue" , text="MOTD: " , bd = 10)
label_MOTD.pack(side=LEFT)

entry_MOTD = Entry(frame_MOTD, width = 80 , bd = 10 )
entry_MOTD.insert(0,'This is a restricted area ... GET OUT NOW ... Cyber dogs online')
entry_MOTD.pack(side=RIGHT)



def take_inputs():
	user_name = entry_user_name.get()
	password = entry_PW.get()
	enable_PW = entry_enable_PW.get()
	IP_num = entry_IP.get()
	mask = entry_mask.get()
	port_type = entry_port_type.get()
	port_num = entry_port_num.get()
	host_name = entry_Host_Name.get()
	motd = entry_MOTD.get()

	print(user_name)
	print(password)
	print(enable_PW)
	print(IP_num)
	print(mask)
	print(port_type)
	print(port_num)
	print(host_name)
	print(motd)

	path_get = entry_select_path.get()

	# file = open("E:/python_projects/Python_For_Networking_Course/Initial_Configration_GUI.txt" , "w")
	file = open(f"{path_get}/Initial_Configration_GUI.txt" , "w")

	file.write(f"""

enable 
	configure terminal
		username {user_name} password {password}
		enable password {enable_PW}

		interface {port_type} {port_num}
			no shutdown
			ip address {IP_num} {mask}
			exit 

		hostname {host_name}
		banner motd #{motd}#
		exit
	exit
exit

	""")


	file.close()


	
frame_button = Frame(master , bd = 10 , bg = "green")
frame_button.place(x=250, y=500+a)

button = Button(frame_button, text = " Submit ", command = take_inputs ,
			 	fg = "black", font = "Times", 
			 	bg = "light blue" )
button.pack()



master.title("Initial Configration")
master.mainloop()
