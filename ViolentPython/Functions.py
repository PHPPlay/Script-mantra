#!/usr/bin/python

import socket

def retBanner(ip, port):

    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):

    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print '[+] FreeFloat FTP Server is vulnerable.'

    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print '[+] 3CDaemon FTP Server is vulnerable.'
    elif 'Ability Server 2.34' in banner:
            print '[+] Ability FTP Server is vulnerable.'
    elif 'Sami FTP Server 2.0.2' in banner:
            print '[+] Sami FTP Server is vulnerable.'
    else:
        print '[-] FTP Server is not vulnerable.'
        return

def main():

    ftp_server = str(raw_input("Please enter the ftp server: "))
    port_num = int(input("Please enter the port number: "))
    ftp_server1 = str(raw_input("Please enter the ftp server: "))
    port_num1 = int(input("Please enter the port number: "))
    banner1 = retBanner(ftp_server, port_num)
    if banner1:
        print '[+] '+ ftp_server + ':' + banner1.strip('\n')
        checkVulns(banner1)
    banner2 = retBanner(ftp_server1, port_num1)
    if banner2:
        print '[+]' + ftp_server1 + ':' + banner2.strip('\n')
        checkVulns(banner2)

if __name__ == '__main__':
    main()


