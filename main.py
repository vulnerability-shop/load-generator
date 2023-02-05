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
#import smtplib
#
#server = smtplib.SMTP('10.0.2.4')
#server.set_debuglevel(1)
#server.login('msfadmin', 'msfadmin')
#server.quit()


# dns using dnspython
# https://github.com/rthalley/dnspython
# ISC License
# https://github.com/rthalley/dnspython/blob/master/LICENSE
#import dns.message
#import dns.rdataclass
#import dns.rdatatype
#import dns.query
#
#qname = dns.name.from_text("google.com")
#q = dns.message.make_query(qname, dns.rdatatype.NS)
#print("The query is:")
#print(q)
#print("")
#r = dns.query.udp(q, "10.0.2.4")
#print("The response is:")
#print(r)
#print("")
#print("The nameservers are:")
#ns_rrset = r.find_rrset(r.answer, qname, dns.rdataclass.IN, dns.rdatatype.NS)
#for rr in ns_rrset:
#    print(rr.target)
#print("")
#print("")


# rpc port 111 (SUN Remote Procedure Call)
# https://docs.python.org/3/library/xmlrpc.client.html
# simple test program (from the XML-RPC specification)
#from xmlrpc.client import ServerProxy, Error
#
#with ServerProxy("http://10.0.2.4:111/") as proxy:
#    print(proxy)


