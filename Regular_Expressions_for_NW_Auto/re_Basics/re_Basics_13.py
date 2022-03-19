import re



# Only use lookahed method to print ‘http’
m = (re.search(r"\w{4,5}(?=:)", "http://www.cisco.com/techsupport"))
print(m.group())



# Only use lookahed and lookbehind method to print ‘www.cisco.com’
import re
m = (re.search(r"(?<=\/)\w.+[.]\w+[.]\w+(?=/)", "http://www.cisco.com/techsupport"))
print(m.group())


# match all file types using regular expression - .*[.].*$
import re
expr = "vlan.dat\nsw1.bak\nconfig.text\npynetauto.dat\nsw1_old.bak\n2960x-universalk9-mz.152-2.E6.bin"
m = re.findall(".*[.].*$", expr, re.M)
print(m)