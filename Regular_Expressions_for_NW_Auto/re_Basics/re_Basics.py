import re 

expr = ". ^ $ * + ? \ | ( ) { } [ ]"

print( re.search(r'[\^]' , expr) )

print( re.search(r'[\*]' , expr) )

print( re.search(r'[\.]' , expr) )

print( re.search(r'[;]' , expr) )

print( re.search('[*]' , expr) )

print( re.search("[.]" , expr) )


print( re.findall('[^a4]' , "adfagajaiala;apajatba6a5855a444a") )

print( re.search(r'[\\]' , expr) )

print( re.search(r'[\]]' , expr) )

p = re.compile('d.g' , re.DOTALL)
m = p.match("d\ng") 
print(m)
m = p.match("dfffg")
print(m)