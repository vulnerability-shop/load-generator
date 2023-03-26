# ftplib
# https://www.tutorialspoint.com/python_network_programming/python_ftp.htm
import ftplib
 
ftp = ftplib.FTP("10.0.2.4")
ftp.login("msfadmin", "msfadmin")
print(ftp.nlst())
ftp.quit()
