#!/usr/bin/python

try:
    print "[+] 1337/0 =" + str(13370/0)
except Exception, error:
    print "[-] Error =" +str(error)
