str1 = input("Enter The Word:")

file = open("E:/python_projects/Python_For_Networking_Course/file_handling/text.txt" , "r")

for line in file:
    if str1 in line:
        print(line)
        

file.close()