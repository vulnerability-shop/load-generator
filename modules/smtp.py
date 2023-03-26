# smtp
# https://docs.python.org/3/library/smtplib.html
import smtplib

server = smtplib.SMTP('10.0.2.4')
server.set_debuglevel(1)
server.login('msfadmin', 'msfadmin')
server.quit()