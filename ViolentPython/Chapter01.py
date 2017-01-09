#!/usr/bin/python
banner = "Welcome to Python"
print banner.lower()
print banner.upper()
print banner.replace('Python', 'Perl')
list = []
portList = []
portList.append(21)
print portList
portList.append(22)
print portList
portList.append(80)
portList.append(443)
print portList
portList.append('Rafi')
print portList
print portList.index(80)
portList.remove('Rafi')
print portList
cnt = len(portList)
print cnt
print "[+] Scanning " + str(cnt) + " Total Ports"

print "\n[+] Let's work on the dictonary\n\r"

services = {'ftp' : 21, 'ssh' : 22, 'smtp' : 25, 'http' : 80, 'IMAP' : 143}
print "Printing ... the dictonary list " + str(services)

print services.keys()
print services.items()
print services.has_key('ftp')
print services.values()
print "[+] Found vuln with FTP on port " + str(services['ftp'])
