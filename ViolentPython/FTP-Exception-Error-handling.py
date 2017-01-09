#!/usr/bin/python

import socket
socket.setdefaulttimeout(2)
s = socket.socket()

ftp_server = str(raw_input("Please enter the ftp server name: "))
port_num = int(input("Please enter the ftp port number: "))
try:
    s.connect((ftp_server, port_num))
    ftp_response = s.recv(1024)
    print "[+] Response from the server[+] : " + str(ftp_response)
except Exception, error_ftp:
    print "[-] Sorry the error is : " + str(error_ftp)
