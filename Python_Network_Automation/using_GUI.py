from tkinter import *

master = Tk()

master.geometry("300x300")
master.title("ospf")

label_1 = Label(master , text="Enter IP: ")
label_1.pack()

entry_1 = Entry(master)
entry_1.pack()
entry_1.get()



def take_action():
	ip = entry_1.get()
	file = open("E:\\python_projects\\Python_For_Networking_Course\\test_GUI.txt" , "w")
	file.write(f"router ospf 1\n\t network {ip}")

	file.close()

	# print(ip)
	

button_1 = Button(master, text = "print the IP: ", command = take_action )
button_1.pack()





master.mainloop()