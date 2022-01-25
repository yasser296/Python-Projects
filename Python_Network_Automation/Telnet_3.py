vlan_num = input("vlan num: ")
ip_mask = input("Enter ip & mask: ")


configration = f"interface vlan {vlan_num} \n\t no shutdown \n\t ip address {ip_mask} \n\t"


print(configration)

