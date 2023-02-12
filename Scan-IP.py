import socket
from time import *

ip = input ("enter-ip > ")
print("scanning for " + ip)

openPorts = []
openServs = []

ports = [20   , 21   , 22   , 23      , 25    , 26     , 50     , 51     , 53      , 67    , 68    , 69    , 80    , 110   , 119   , 123  , 135      , 139      , 143    , 161   , 162   , 389   , 443    , 445           , 465    , 587         , 902     , 912        , 989      , 990      , 993    , 995    , 1521    , 2179   , 2222          , 3306   , 3389 , 8080        ]
servs = ["ftp", "ftp", "ssh", "telnet", "smtp", "rsftp", "ipsec", "ipsec", "domain", "DHCP", "dhcp", "TFTP", "http", "pop3", "NNTP", "NTP", "NetBIOS", "NetBIOS", "imap4", "SNMP", "SNMP", "LDAP", "https", "microsoft-ds", "smtps", "submission", "VMware", "apex-mesh", "ftp\ssl", "ftp\ssl", "imap3", "pop3s", "oracle", "vmrdp", "EtherNetIP-1", "MySQL", "RDP", "http-proxy"]

try:
	for i in range(0,len(ports) - 1):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if(s.connect_ex((ip,ports[i]))==0):
			serv=servs[i]
			openPorts.append(ports[i])
			openServs.append(servs[i])
			print("port %s open %s service"%(ports[i],servs[i]))
	print("completed scan...")
except KeyboardInterrupt:
	sleep(0.125)

x = input("Do-you-want-save-scan? > ")
if x.lower() == "y" or x.lower() == "yes":
	target = input("enter-target-name")
	fl = open(target + "-scan-file.txt","a")
	fl.write("Scan for " + target + "\n")
	fl.write("IP address is " + ip + "\n")
	for i in range(0, len(openPorts) - 1):
		fl.write(openPorts[i] + " open " + openServs[i] + "\n")
	fl.close()
	print("Scan saved in %s-scan-file.txt file" %(target))