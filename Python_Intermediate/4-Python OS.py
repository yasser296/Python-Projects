import os


# # current working directory
# current_working_directory = os.getcwd()
# print(current_working_directory)
# print(type(current_working_directory))



# # changes the current working directory of the program
# change_dir = os.chdir("D://")
# print(os.getcwd())


# # The os.mkdir function creates an empty directory of a specified file path. 
# # The end result in this example will basically be a new folder at
# # the file path “C:/Users/Default”.
# os.mkdir("E://python_projects/Python_Intermediate/new_folder")

# for i in range(0 , 10):
# 	os.mkdir("E://python_projects/Python_Intermediate/new_folder/folder_%d" %i )



# # The os.listdir function lists the contents of each individual file and folder in a given directory. 
# # The following code will proceed to print out the paths of every single file, folder and subfolder individually.

# list_of_file_names = os.listdir("E://python_projects/Python_Intermediate/new_folder")
# print(list_of_file_names)
# print(type(list_of_file_names))





# # The os.walk walks through all the folders and subfolders in a directory. 
# # This function comes in handy when searching through your computer for files. 
# # Run the code below to truly understand how this function works.



# for folder, subfolders, files in os.walk("E://python_projects/Python_Intermediate/new_folder"):
# 	print(folder)


# 	for subfolder in subfolders:
# 		print(subfolder)

# 	for file in files:
# 		print(file)


# # The os.walk function returns three values. A folder’s file path, 
# # the names of the sub-folders in it, and the names of the files within the
# # sub-folders. If you’re creative you can play around with this function to achieve many things.



############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################




# Another handy function is startfile(). This function takes two parameters, a file path and an operation. 
# The file path is compulsory, whereas we can leave the operation to it’s default value.
# When passing in a single parameter, the startfile() opens the file at the file path you gave, 
# just like you would regularly open/run it (by double clicking). 
# The below code will open up the “kitten.jpg” image in the default image viewer installed on any computer.


# os.startfile("I-V_characteristic_dpi=400.png")


# If you give it the path to an exe, the exe will be executed. 
# If you give it the path of a .py file, it will also be executed. startfile() is a simple but powerful function.
# Examples of other operations include “print” and “edit” (for files) and “explore” and “find” (for directories/folders). 
# (These are placed in the second parameter).








# OS library has the ability to open files to read and write data to them. 
# The default mode is the read state, denoted by ‘r’. The other state is the write file, 
# denoted by ‘w’. The os.popen() takes 2 parameters. 
# The first is the name of the file to be read/written to, and the second is the mode.



# File = os.popen("test.txt", 'w')
# File.write("Hello World")
# File.close

# File = os.popen("test.txt", 'r')
# print(File.read())
# File.close

# os.close(1)






############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################




# os.rename("test.txt","New_test.txt")



############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################


# Misc. Functions
# The os.getlogin() functions returns the name of the user logged in on the controlling terminal of the process

user_name = os.getlogin()
print(user_name)

