#!/usr/bin/python
import socket

def retBanner(ip, port):

    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception, error:
        print "[-] Error = " +str(error)
        return

def CheckVulns(banner):
    f = open("FTPvuln", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: " + banner.strip('\n')
        else:
            print "[+] Server is Secure " + banner.strip('\n')

def main():

    ftp_server = str(raw_input("Please enter the ftp server: "))
    port_num = int(input("Please enter the port number: "))
    banner = retBanner(ftp_server, port_num)
    CheckVulns(banner)

if __name__ == '__main__':
    main()