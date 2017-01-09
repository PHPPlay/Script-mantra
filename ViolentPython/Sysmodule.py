#!/usr/bin/python

import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    print "[+] Reading Vulnerbilites From: " + filename + '\n'
    f = open("FTPvuln", 'r')
    for line in f.readlines():
        print   line.strip('\n')