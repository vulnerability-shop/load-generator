#from requests2 import http_legit
#r = http_legit.do_http_basic("http://10.0.2.4/")
#print(r)


# SSH using paramiko
# https://stackoverflow.com/a/63240897
# GNU Lesser General Public License v2.1
# https://github.com/paramiko/paramiko/blob/main/LICENSE
#import paramiko
#
#host = "10.0.2.5"
#port = 22
#username = "root"
#password = "PfeH2023"
#
#command = "ls"
#
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(host, port, username, password)
#
#stdin, stdout, stderr = ssh.exec_command(command)
#lines = stdout.readlines()
#print(lines)


# ftplib
# https://www.tutorialspoint.com/python_network_programming/python_ftp.htm
#import ftplib
# 
#ftp = ftplib.FTP("10.0.2.4")
#ftp.login("msfadmin", "msfadmin")
#print(ftp.nlst())
#ftp.quit()


# telnet
# https://docs.python.org/3/library/telnetlib.html
#from telnetlib import Telnet
#with Telnet('10.0.2.4', 23) as tn:
#    tn.interact()


# smtp
# https://docs.python.org/3/library/smtplib.html
import smtplib

server = smtplib.SMTP('10.0.2.4')
server.set_debuglevel(1)
server.login('msfadmin', 'msfadmin')
server.quit()


