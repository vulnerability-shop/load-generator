# SSH using paramiko
# https://stackoverflow.com/a/63240897
# GNU Lesser General Public License v2.1
# https://github.com/paramiko/paramiko/blob/main/LICENSE
import paramiko

host = "10.0.2.5"
port = 22
username = "root"
password = "PfeH2023"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
