from zipfile import *

Zippy = ZipFile("Backup.zip", 'w')

# this to make zip for the all folders name and save the "test.txt" file onle
# Zippy.write("E:/python_projects/ZIP_Files/test.txt")

# this to make zip for the "test.txt" file onle     
Zippy.write("test.txt")
Zippy.close()