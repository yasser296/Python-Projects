file = open("mailbox.txt" , "r")
counter = 0 
for line in file :
	if line.startswith("From "):
		counter += 1
		print(line.strip().split("From ")[1].split()[0])
		print(line)
print("There were" , counter , "sender email address.")













