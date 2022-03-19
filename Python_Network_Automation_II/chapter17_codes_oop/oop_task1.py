class Pynetauto_co: # parent class of Cisco class
    "Parent class of Cisco, HP, Juniper, Arista"
    def __init__(self, companyname):
        self.companyname = companyname
    def PrintInfo_P1(self):
        print("Pynetauto Company")
        #print("www.xyzptyltd.com")

class Cisco(Pynetauto_co): # parent class of Devices class
    "Parent class of Switch, Router and Firewall"
    def __init__(self, vendor):
        self.Vendor = vendor
    def PrintInfo_P2(self):
        print("Cisco")
        #print("www.cisco.com")

class Devices (Cisco): # parent class of Router and Switch classes
    "Parent class of Switch, Router and Firewall"
    def __init__(self, serialnumber, hostname, ipaddress, modelnumber, devicetype):
        self.serialnumber = serialnumber # 12 Hexadecimal numbers
        self.hostname = hostname
        self.ipaddress = ipaddress # format 1.0.0.X - 254.254.254.XXX
        self.modelnumber = modelnumber
        self.devicetype = devicetype
    def show(self): # show all the attributes
        print(f"{self.serialnumber},{self.hostname},{self.ipaddress},{self.modelnumber},{self.devicetype}")

class Router(Devices):  
    def process(self):
        print("Packet switching")
class Switch(Devices):
    def process(self):
        print("Packet routing")

rt3 = Router("000111222222", "RT03", "2.2.2.2", "C4351/K9", "RT")            
sw3 = Switch("000111222111", "SW03", "1.1.1.1", "WS-3850-48T", "SW")

rt3.PrintInfo_P1()
rt3.PrintInfo_P2()
rt3.show()

sw3.PrintInfo_P1()
sw3.PrintInfo_P2()
sw3.show()
