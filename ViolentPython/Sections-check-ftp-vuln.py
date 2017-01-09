#!/usr/bin/python

import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("ftp.microsoft.com", 21))
ans = s.recv(1024)
if ("FreeFloat FTP server (Version 1.00" in ans):
    print "[+] FreeFloat FTP server is vulnerble"
elif ("3Com 3CDaemon FTP server version 2.0" in ans):
    print ("[+] 3CDaemon FTP server is vulnerable")
else:
    print("[+] Microsoft FTP server is not vulnerble")