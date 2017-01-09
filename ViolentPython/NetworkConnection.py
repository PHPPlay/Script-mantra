#!/usr/bin/python
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("ftp.microsoft.com", 21))
ans =  s.recv(1024)
print ans
