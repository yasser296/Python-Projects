import re 

print( re.match('[a-z]+' , "configuration register is 0x2102").group() )

print( re.match('[a-z]+' , "configuration register is 0x2102").start() )

print( re.match('[a-z]+' , "configuration register is 0x2102").end() )

print( re.match('[a-z]+' , "configuration register is 0x2102").span() )



print( re.match('[a-z]+' , "configuration register is 0x2102").group )      # object location in the memory

print( re.match('[a-z]+' , "configuration register is 0x2102").start )

print( re.match('[a-z]+' , "configuration register is 0x2102").end )

print( re.match('[a-z]+' , "configuration register is 0x2102").span )


