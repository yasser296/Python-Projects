str1 = "ospf"

show = open("C:/Users/My PC/Desktop/text.txt" , "r")


file = show.read()

if str1 in file :
    print("found")
else:
    print("not found")


show.close()