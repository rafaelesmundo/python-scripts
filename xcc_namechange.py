from netmiko import ConnectHandler
import csv
import getpass
import time


#User input
print("Please Provide the following information: ")
file_name = input("Input file: ")
controller_ip1 = input("Controller 1 IP: ")
#controller_ip2 = input("Controller 2 IP: ")
controller_username = input("Username: ")
controller_password = getpass.getpass("Password: ")

extremehandle1 = {
	'device_type': 'extreme',
    'host':   controller_ip1,
    'username': controller_username,
    'password': controller_password,
    'session_log': 'log_controller1.out'
}

#connect to controller
net_connect1 = ConnectHandler(**extremehandle1)
#enter ap mode
apmode1 = net_connect1.send_command("ap",expect_string='#')
start_time = time.time()
print(start_time)

#Informational Countdown
print("Please Wait....Changing the names of APs on Controller")

#read file and update AP name
with open(file_name, newline='') as csvfile1:
	reader1 = csv.DictReader(csvfile1)
	for row in reader1:
		ap_serial1 = net_connect1.send_command(row['serial'])
		name_ap1 = net_connect1.send_command("name " + row['apname'])
		apply_name1 = net_connect1.send_command("apply")
		exit_serial1 = net_connect1.send_command("ap",expect_string='#')

print("AP Name Update is Complete")
end_time = time.time()
print(end_time)
total_time = end_time - start_time
total_time = total_time / 60
print(total_time)