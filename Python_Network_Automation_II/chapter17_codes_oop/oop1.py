# class Router:
#     def __init__(self, serialnumber, hostname, ipaddress, modelnumber, devicetype):
#         self.serialnumber = serialnumber # 12 Hexadecimal numbers
#         self.hostname = hostname
#         self.ipaddress = ipaddress # format 1.0.0.X - 254.254.254.XXX
#         self.modelnumber = modelnumber
#         self.devicetype = devicetype
#     def process(self):
#         print("Packet routing")

# class Switch:
#     def __init__(self, serialnumber, hostname, ipaddress, modelnumber, devicetype):
#         self.serialnumber = serialnumber # 12 Hexadecimal numbers
#         self.hostname = hostname
#         self.ipaddress = ipaddress # format 1.0.0.X - 254.254.254.XXX
#         self.modelnumber = modelnumber
#         self.devicetype = devicetype
#     def process(self):
#         print("Packet switching")


#####################################################################
#####################################################################
#####################################################################


class Devices:
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
        print("Packet routing")

class Switch(Devices):
    def process(self):
        print("Packet switching")

class Firewall(Devices):
    def process(self):
        print("Packet filtering")

rt1 = Router("001122AABBCC", "RT01", "1.1.1.1", "C4431-K9", "RT")
sw1 = Switch("001122DDEEFF", "SW02", "2.2.2.2", "WS-3850-48T", "SW")
fw1 = Firewall("003344ABCDEF", "FW02", "3.3.3.3", "PA-5280", "FW")

rt1.show()
rt1.process()

sw1.show()
sw1.process()

fw1.show()
fw1.process()

