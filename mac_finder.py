#Raf
#mac_finder.py
#Helps you find the Port a MAC Adress is on with Extreme VOSS,EXOS,AND ERS

from netmiko import ConnectHandler
import getpass

#Info about the Switch and MAC Adderss
switch_ip = input("What is the IP address of the switch: ")
switch_username = input("what is the username: ")
switch_password = getpass.getpass(prompt = "What is the password: ")
mac_address = input("What is the MAC address you are looking for\n Example xx:xx:xx:xx:xx:xx : ")
switch_os_input = input("What type of OS is on the Switch?\n (1)ERS\n (2)EXOS\n (3)VSP\n Please Select a number: ")

#Extreme Platforms that we are accessing
extreme_ers = {
    'device_type': 'extreme_ers',
    'host':   '{}'.format(switch_ip),
    'username': '{}'.format(switch_username),
    'password': '{}'.format(switch_password),
}

extreme_exos = {
    'device_type': 'extreme_exos',
    'host':   '{}'.format(switch_ip),
    'username': '{}'.format(switch_username),
    'password': '{}'.format(switch_password),
}

extreme_vsp = {
    'device_type': 'extreme_vsp',
    'host':   '{}'.format(switch_ip),
    'username': '{}'.format(switch_username),
    'password': '{}'.format(switch_password),
}

#Conditions based on input from user about the os type
if switch_os_input == "1":
    os_type = extreme_ers
    net_connect = ConnectHandler(**os_type)
    output = net_connect.send_command("show mac-address-table address {}".format(mac_address))
elif switch_os_input == "2":
    os_type = extreme_exos
    net_connect = ConnectHandler(**os_type)
    output = net_connect.send_command("show fdb {}".format(mac_address))
elif:
    os_type = extreme_vsp
    net_connect = ConnectHandler(**os_type)
    output = net_connect.send_command("show vlan mac-address-entry mac {}".format(mac_address))
else:
    print("That option was not listed please try again.")

#Print the results
print("\nHere is the Port the MAC address is on:\n")
print(output)
