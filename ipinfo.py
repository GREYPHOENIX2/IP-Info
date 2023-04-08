import requests
import json
import sys
import socket
import time

line = ">"*52
s = " "*10
gr = '\033[1;30m'
g = '\033[0;32m'
b = '\033[0;34m'
y =  '\033[0;33m'
r = '\033[0;31m'

print(g)

print(f"""
{gr}[{r}={gr}]Grey Phoenix
""")


about = f"""{line}
This Tool Will Give you information about \n{s}The Ip Address You Want
{line}{gr}

"""



for letter in about:
	sys.stderr.write(letter)
	sys.stderr.flush()
	time.sleep(0.015)







url = "http://ip-api.com/json/"
def option1():
	print(gr)
	try:
		ip=input ("\nEnter the public IP : ")


		req = requests.get(url+ip)

		data = req.text

		value = json.loads(data)
	

		if value['status'] =="success":
			print("IP : " + value['query'])
			print("ISP : " + value['isp'])
			print("Country : "+value['country'])
			print("county code : " + value['countryCode'])
			print("Region : " + value['region'])
			print("City : " + value['city'])
			print("region name : " + value['regionName'])
			print("Time Zone : " + value["timezone"])
			print("latitude : " + str(value['lat']))
			print("longitude : "+str(value['lon']))
		else:
			print("The IP address is a bogon IP. No data for this IP address.")	
	except:
		print("Make sure you have internet connection")
def option2():
	print(gr)
	try:
		req = requests.get(url)

		data = req.text

		value = json.loads(data)
		ip = value['query']
		print(f"Your ip {ip} \n")
	
	
		print("IP : " + value['query'])
		print("ISP : " + value['isp'])
		print("Country : "+value['country'])
		print("county code : " + value['countryCode'])
		print("Region : " + value['region'])
		print("City : " + value['city'])
		print("region name : " + value['regionName'])
		print("Time Zone : " + value["timezone"])
		print("latitude : " + str(value['lat']))
		print("longitude : "+str(value['lon']))
	
	except:
		print("make sure you have internet connection")
	




print(f"1.Enter IP [{r}+{gr}]")

print(f"2.Get your ip information [{r}+{gr}]")
option = int(input(f"Choose an option :{r}"))
print(g)
if option == 1:
	option1()
elif option == 2:
	option2()